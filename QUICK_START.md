# Quick Start Guide

## Getting Started

### 1. Install Dependencies
```bash
npm install
```

### 2. Start Development Server
```bash
npm start
```
The application will open automatically at `http://localhost:3000`

### 3. Backend Setup (FastAPI)
Ensure your FastAPI backend is running on `http://127.0.0.1:8000`

The frontend will send POST requests to: `http://127.0.0.1:8000/predict`

## Project Navigation

### Pages Available
1. **Home** (`/`) - Main landing page
2. **Complaint Form** (`/complaint`) - Submit complaints for prediction
3. **Dashboard** (`/dashboard`) - Analytics and insights
4. **About** (`/about`) - System information
5. **Results** (`/results`) - View prediction results

## File Organization

```
Frontend/
├── public/
│   └── index.html
├── src/
│   ├── components/
│   │   ├── Navbar.js
│   │   ├── Sidebar.js
│   │   ├── ComplaintForm.js
│   │   ├── ResultCard.js
│   │   ├── Charts.js
│   │   └── KPI.js
│   ├── pages/
│   │   ├── Home.js
│   │   ├── Complaint.js
│   │   ├── Dashboard.js
│   │   ├── About.js
│   │   └── Results.js
│   ├── services/
│   │   └── api.js
│   ├── App.js
│   ├── index.js
│   └── styles.css
├── package.json
├── README.md
└── .env.example
```

## Key Features

### Navbar
- Project branding
- Sticky at top
- Purple gradient theme

### Sidebar
- Navigation menu (fixed left)
- Active route highlighting
- Responsive collapse on mobile

### Complaint Form
- Dropdown for products
- Text inputs for issue details
- Textarea for company response
- Form validation
- Character counter
- Submit/Reset buttons
- Loading spinner during processing

### Results Page
- Display all input fields
- Show predicted response
- Display confidence percentage
- Action buttons to submit new complaint or view dashboard

### Dashboard
- 4 KPI cards (Total Complaints, Top Category, Total Products, Frequent Issue)
- 4 Charts:
  - Product Distribution (Pie)
  - Complaint Categories (Bar)
  - Trends Over Time (Line)
  - State-wise Complaints (Bar)

### Styling
- Fully responsive design
- CSS Grid and Flexbox layouts
- Smooth animations and transitions
- Mobile-first approach
- Color scheme: Purple (#667eea) & Violet (#764ba2)

## Environment Configuration

Copy `.env.example` to `.env.local` and update:
```env
REACT_APP_API_URL=http://127.0.0.1:8000
REACT_APP_ENV=development
REACT_APP_ENABLE_ANALYTICS=true
REACT_APP_ENABLE_DUMMY_DATA=true
```

## Build for Production

```bash
npm run build
```

The `build` folder contains the optimized production build ready to deploy.

## Troubleshooting

### Port 3000 Already in Use
```bash
npm start -- --port 3001
```

### Backend Connection Error
- Ensure FastAPI backend is running
- Check API URL: `http://127.0.0.1:8000`
- Check browser console for CORS errors

### Component Not Showing
- Check React DevTools for component tree
- Verify route paths in `App.js`
- Check CSS class names in `styles.css`

## Dependencies Overview

| Package | Version | Purpose |
|---------|---------|---------|
| react | ^18.2.0 | Core library |
| react-dom | ^18.2.0 | DOM rendering |
| react-router-dom | ^6.14.0 | Routing |
| axios | ^1.4.0 | HTTP requests |
| @mui/material | ^5.14.0 | UI components |
| recharts | ^2.8.0 | Charts & graphs |

## Next Steps

1. ✅ Frontend project is ready
2. Connect to FastAPI backend
3. Configure prediction model
4. Test with sample data
5. Deploy to production

## Support

For issues or questions, refer to:
- README.md - Full documentation
- Component files - Inline code comments
- React documentation - https://react.dev
- Material UI docs - https://mui.com

---

**Ready to use!** Start with `npm install && npm start`
