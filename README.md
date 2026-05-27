# Banking Customer Complaint Classification System

## Overview
AI-Based Banking Customer Complaint Classification System - A responsive React frontend that predicts company responses for banking customer complaints using a FastAPI backend.

## Features

### 1. **Home Page**
   - Attractive hero section with project title and description
   - Quick navigation with "Get Started" button
   - Feature highlights showcasing system capabilities

### 2. **Complaint Form Page**
   - Product selection dropdown
   - Issue and Sub-Issue text fields
   - Company Public Response textarea with character counter
   - Form validation
   - Loading spinner during processing
   - Submit and Reset buttons

### 3. **Results Page**
   - Display all input details
   - Show predicted company response
   - Display prediction confidence percentage
   - Status card information
   - Navigation options

### 4. **Analytics Dashboard**
   - **KPI Cards:**
     - Total Complaints
     - Top Complaint Category
     - Total Products
     - Most Frequent Issue
   - **Charts:**
     - Pie chart for product distribution
     - Bar chart for complaint categories
     - Line chart for complaint trends
     - Bar chart for state-wise complaints

### 5. **Sidebar Navigation**
   - Home
   - Complaint Form
   - Dashboard
   - About

## Tech Stack

- **Frontend Framework:** React 18.2.0
- **Routing:** React Router DOM 6.14.0
- **HTTP Client:** Axios 1.4.0
- **UI Components:** Material UI 5.14.0
- **Charts:** Recharts 2.8.0
- **Styling:** CSS3 with Responsive Design
- **State Management:** React Hooks

## Project Structure

```
src/
├── components/
│   ├── Navbar.js          # Navigation bar component
│   ├── Sidebar.js         # Sidebar navigation
│   ├── ComplaintForm.js   # Complaint form component
│   ├── ResultCard.js      # Result display component
│   ├── Charts.js          # Charts component with Recharts
│   └── KPI.js             # KPI cards component
├── pages/
│   ├── Home.js            # Home page
│   ├── Complaint.js       # Complaint form page
│   ├── Dashboard.js       # Analytics dashboard
│   ├── About.js           # About page
│   └── Results.js         # Results page
├── services/
│   └── api.js             # API calls with Axios
├── App.js                 # Main app component
├── index.js               # React DOM render
└── styles.css             # Global styles
public/
└── index.html             # HTML template
```

## Installation & Setup

### Prerequisites
- Node.js (v14 or higher)
- npm or yarn

### Steps

1. **Install dependencies:**
   ```bash
   npm install
   ```

2. **Start the development server:**
   ```bash
   npm start
   ```
   The application will open at `http://localhost:3000`

3. **Build for production:**
   ```bash
   npm run build
   ```

## API Integration

### Prediction Endpoint
**POST** `http://127.0.0.1:8000/predict`

**Request Format:**
```json
{
  "product": "Credit card",
  "issue": "Billing error",
  "sub_issue": "Unexpected charges",
  "company_public_response": "We are investigating your complaint..."
}
```

**Response Format:**
```json
{
  "predicted_response": "Corrected error and refunded amount",
  "confidence": 0.95,
  "status": "RESOLVED"
}
```

## Features & Components

### ComplaintForm Component
- Real-time form validation
- Character counter for textarea
- Loading state management
- Error handling
- Session storage for results

### Charts Component
- Product distribution pie chart
- Complaint categories bar chart
- Complaint trends line chart
- State-wise complaints bar chart
- Responsive design with Recharts

### KPI Component
- Four KPI cards with dynamic data
- Color-coded indicators
- Emoji icons for visual appeal

### ResultCard Component
- Displays prediction results
- Shows confidence percentage
- Displays all input fields
- Responsive layout

## Responsive Design

The application is fully responsive with breakpoints for:
- Desktop (1200px and above)
- Tablet (768px - 1199px)
- Mobile (480px - 767px)
- Small Mobile (below 480px)

## Styling Highlights

- **Color Scheme:** Purple gradient (#667eea to #764ba2)
- **Modern UI:** Clean cards with shadows
- **Accessibility:** Good contrast ratios
- **Animations:** Smooth transitions and hover effects
- **Typography:** Roboto font family

## Dummy Data

The dashboard uses sample data for initial demonstration:
- 12,456 total complaints
- 8 product categories
- 5 main complaint categories
- 6-month trend data
- State-wise complaint distribution

## State Management

All state is managed using React Hooks:
- `useState` for component state
- `useNavigate` for routing
- `useLocation` for active route detection
- `useEffect` for side effects

## Error Handling

- Form validation with error messages
- API error handling with user-friendly messages
- Session storage for result persistence
- Fallback UI for missing data

## Future Enhancements

- Backend integration with FastAPI
- Real-time data updates
- Export reports functionality
- User authentication
- Advanced filtering options
- Historical data tracking
- API documentation

## Browser Support

- Chrome (latest)
- Firefox (latest)
- Safari (latest)
- Edge (latest)

## Deployment

To deploy:

1. Build the project:
   ```bash
   npm run build
   ```

2. Deploy the `build` folder to your hosting service:
   - Vercel
   - Netlify
   - AWS S3
   - GitHub Pages

## License

This project is proprietary and intended for financial institutions.

## Support

For issues or questions, please contact the development team.

---

**Note:** Ensure the FastAPI backend is running on `http://127.0.0.1:8000` for the prediction functionality to work.
