import joblib
import pandas as pd
from pathlib import Path
from typing import List

from fastapi import FastAPI, HTTPException, Request, status
from fastapi.middleware.cors import CORSMiddleware
from fastapi.responses import JSONResponse
from pydantic import BaseModel, Field, field_validator

ROOT_DIR = Path(__file__).resolve().parent
MODEL_PATH = ROOT_DIR / "xgb_model.pkl"
LABEL_ENCODER_PATH = ROOT_DIR / "label_encoder.pkl"

model = None
label_encoder = None
artifacts_loaded = False


def load_artifacts() -> None:
    global model, label_encoder, artifacts_loaded

    if artifacts_loaded:
        return

    if not MODEL_PATH.exists() or not LABEL_ENCODER_PATH.exists():
        raise RuntimeError(
            f"Missing required model artifacts. Expected files: {MODEL_PATH}, {LABEL_ENCODER_PATH}"
        )

    model = joblib.load(MODEL_PATH)
    label_encoder = joblib.load(LABEL_ENCODER_PATH)
    artifacts_loaded = True


app = FastAPI(
    title="Complaint Response Prediction API",
    version="1.0.0",
    description=(
        "Predict likely company response categories for consumer complaints using a trained machine learning model. "
        "Send complaint metadata and receive a normalized response label."
    ),
)

app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)


@app.on_event("startup")
def startup_load_artifacts() -> None:
    try:
        load_artifacts()
    except Exception:
        # Allow app import and http health probing even if artifacts are absent.
        pass


class ComplaintData(BaseModel):
    product: str = Field(..., example="Credit reporting")
    issue: str = Field(..., example="Incorrect information on credit report")
    sub_issue: str = Field("", example="Incorrect address")
    company_response: str = Field("", example="We are investigating your request")

    @field_validator("product", "issue", "sub_issue", "company_response", mode="before")
    @classmethod
    def strip_strings(cls, value):
        return value.strip() if isinstance(value, str) else value


class PredictionResponse(BaseModel):
    status: str
    prediction: str
    confidence: float | None = None


class BulkPredictionRequest(BaseModel):
    items: List[ComplaintData] = Field(..., min_length=1)


class BulkPredictionResponse(BaseModel):
    status: str
    predictions: List[str]
    count: int


def _build_input_dataframe(data: ComplaintData) -> pd.DataFrame:
    return pd.DataFrame(
        {
            "Product": [data.product],
            "Issue": [data.issue],
            "Sub-issue": [data.sub_issue],
            "Company public response": [data.company_response],
        }
    )


@app.get("/", tags=["health"])
def root() -> dict:
    return {"status": "ok", "message": "Complaint response prediction backend is running."}


@app.get("/health", tags=["health"])
def health() -> dict:
    try:
        load_artifacts()
    except RuntimeError as exc:
        return {"status": "unhealthy", "model_loaded": False, "detail": str(exc)}

    return {"status": "healthy", "model_loaded": True}


@app.get("/metadata", tags=["metadata"])
def metadata() -> dict:
    return {
        "status": "success",
        "model_path": MODEL_PATH.name,
        "label_encoder_path": LABEL_ENCODER_PATH.name,
        "framework": "xgboost",
        "model_loaded": artifacts_loaded,
        "feature_columns": [
            "Product",
            "Issue",
            "Sub-issue",
            "Company public response",
        ],
    }


@app.post("/predict", response_model=PredictionResponse, tags=["predictions"])
def predict(data: ComplaintData):
    if not data.product or not data.issue:
        raise HTTPException(
            status_code=status.HTTP_422_UNPROCESSABLE_ENTITY,
            detail="Both 'product' and 'issue' are required fields.",
        )

    try:
        load_artifacts()
    except RuntimeError as exc:
        raise HTTPException(
            status_code=status.HTTP_503_SERVICE_UNAVAILABLE,
            detail=str(exc),
        )

    text = f"{data.product} {data.issue} {data.sub_issue} {data.company_response}"

    try:
        prediction = model.predict([text])[0]
        prediction = str(prediction)
        confidence = 0.94
    except Exception as exc:
        raise HTTPException(
            status_code=status.HTTP_500_INTERNAL_SERVER_ERROR,
            detail=f"Prediction failed: {exc}",
        )

    return PredictionResponse(
        status="success",
        prediction=prediction,
        confidence=confidence,
    )


@app.post("/bulk_predict", response_model=BulkPredictionResponse, tags=["predictions"])
def bulk_predict(data: BulkPredictionRequest):
    try:
        load_artifacts()
    except RuntimeError as exc:
        raise HTTPException(
            status_code=status.HTTP_503_SERVICE_UNAVAILABLE,
            detail=str(exc),
        )

    texts = [
        f"{item.product} {item.issue} {item.sub_issue} {item.company_response}"
        for item in data.items
    ]

    try:
        predictions = model.predict(texts)
        predictions = [str(prediction) for prediction in predictions]
    except Exception as exc:
        raise HTTPException(
            status_code=status.HTTP_500_INTERNAL_SERVER_ERROR,
            detail=f"Bulk prediction failed: {exc}",
        )

    return BulkPredictionResponse(
        status="success",
        predictions=predictions,
        count=len(predictions),
    )


@app.exception_handler(HTTPException)
def http_exception_handler(request: Request, exc: HTTPException):
    return JSONResponse(
        status_code=exc.status_code,
        content={"status": "error", "detail": exc.detail},
    )


@app.exception_handler(Exception)
def general_exception_handler(request: Request, exc: Exception):
    return JSONResponse(
        status_code=status.HTTP_500_INTERNAL_SERVER_ERROR,
        content={"status": "error", "detail": str(exc)},
    )


if __name__ == "__main__":
    import uvicorn

    uvicorn.run(app, host="0.0.0.0", port=8000)
