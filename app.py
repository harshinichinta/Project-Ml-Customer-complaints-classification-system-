import streamlit as st
import pandas as pd
import joblib

# Load trained model and label encoder
model = joblib.load("xgb_model.pkl")
label_encoder = joblib.load("label_encoder.pkl")

st.set_page_config(
    page_title="Bank Complaint Response Prediction",
    page_icon="🏦",
    layout="centered"
)

st.title("🏦 Customer Complaint Response Prediction")
st.write(
    "Predict the company response based on complaint details."
)

# Input fields
product = st.text_input("Product")
issue = st.text_input("Issue")
sub_issue = st.text_input("Sub-Issue")
company_public_response = st.text_area("Company Public Response")

if st.button("Predict Response"):

    if product and issue:

        input_df = pd.DataFrame({
            "Product": [product],
            "Issue": [issue],
            "Sub-issue": [sub_issue],
            "Company public response": [company_public_response]
        })

        prediction = model.predict(input_df)

        predicted_response = label_encoder.inverse_transform(prediction)[0]

        st.success(
            f"Predicted Company Response: **{predicted_response}**"
        )

    else:
        st.warning("Please enter Product and Issue.")