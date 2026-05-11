# Smart Finance Dashboard Frontend

Next.js frontend for the Smart Finance Dashboard that provides a user interface for transaction category prediction using machine learning.

## Project Structure

```
frontend/
├── src/
│   └── app/
│       ├── predict/
│       │   └── page.tsx          # Main prediction page
│       ├── page.tsx              # Landing page
│       ├── layout.tsx            # Root layout
│       └── globals.css           # Global styles
├── package.json                  # Dependencies
├── next.config.ts               # Next.js configuration
├── tailwind.config.ts           # Tailwind CSS configuration
└── README.md                    # This file
```

## Features

- **Modern UI**: Clean, responsive design with Tailwind CSS
- **TypeScript**: Full type safety throughout the application
- **Real-time Predictions**: Instant ML predictions with confidence scores
- **Error Handling**: Comprehensive error states and user feedback
- **Loading States**: Visual feedback during API calls
- **Responsive Design**: Works perfectly on desktop and mobile devices

## Technology Stack

- **Framework**: Next.js 14 with App Router
- **Language**: TypeScript
- **Styling**: Tailwind CSS
- **State Management**: React useState hooks
- **API Integration**: Fetch API with proper error handling

## Getting Started

### Prerequisites

1. Make sure the FastAPI backend is running on `http://localhost:8000`
2. Node.js 18+ installed

### Installation

1. Install dependencies:
```bash
npm install
```

2. Start the development server:
```bash
npm run dev
```

3. Open [http://localhost:3000](http://localhost:3000) in your browser

## Pages

### 1. Landing Page (`/`)

- **Hero Section**: Introduction to the Smart Finance Dashboard
- **Features**: Overview of key capabilities
- **Technology Stack**: Information about frontend and backend technologies
- **Quick Demo**: Sample predictions to showcase functionality
- **Call-to-Action**: Button to navigate to the prediction page

### 2. Prediction Page (`/predict`)

The main interface for transaction categorization:

#### Input Section
- **Text Input**: Field for entering transaction descriptions
- **Placeholder**: "e.g., Grab Food, Netflix, Shopee, Salary"
- **Validation**: Real-time validation and error messages
- **Submit Button**: Predict Category button with loading state

#### Results Section
- **Original Description**: Shows the entered transaction description
- **Predicted Category**: Displays the ML model prediction
- **Confidence Score**: Shows prediction confidence as percentage with color coding
- **Visual Indicators**: Progress bar and confidence badges
- **Action Buttons**: "Try Another" and "Copy Result" options

## API Integration

The frontend communicates with the FastAPI backend at `http://localhost:8000`:

### Prediction Endpoint
```typescript
POST /predict-category
Content-Type: application/json

Request:
{
  "description": "Grab Food"
}

Response:
{
  "description": "Grab Food",
  "predicted_category": "Food",
  "confidence": 0.7146
}
```

## Usage Examples

1. **Navigate to**: http://localhost:3000
2. **Click "Try Transaction Predictor"** or go to http://localhost:3000/predict
3. **Enter a transaction description** like "Grab Food", "Netflix", "Shopee", or "Salary"
4. **Click "Predict Category"** to see the ML prediction
5. **View results** with confidence scores and visual indicators

## Error Handling

- **Network Errors**: Displays connection issues
- **API Errors**: Shows backend error messages
- **Validation Errors**: Handles empty or invalid inputs
- **Loading States**: Prevents duplicate requests during processing

## Styling

### Design Features
- **Responsive Design**: Mobile-first approach
- **Color Coding**: 
  - Green (80%+): High confidence
  - Yellow (60-79%): Medium confidence
  - Red (<60%): Low confidence
- **Animations**: Smooth transitions and fade-in effects
- **Modern UI**: Clean gradients and shadows

## Development

### Code Quality
- **TypeScript**: Strict type checking enabled
- **ESLint**: Configured for Next.js best practices
- **Component Structure**: Clear separation of concerns
- **Error Boundaries**: Proper error handling throughout

## Deploy on Vercel

The easiest way to deploy your Next.js app is to use the [Vercel Platform](https://vercel.com/new?utm_medium=default-template&filter=next.js&utm_source=create-next-app&utm_campaign=create-next-app-readme) from the creators of Next.js.

Check out our [Next.js deployment documentation](https://nextjs.org/docs/app/building-your-application/deploying) for more details.
