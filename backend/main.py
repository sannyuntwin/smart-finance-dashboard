"""
FastAPI Backend for Smart Finance Dashboard ML Model
This API exposes the transaction category prediction model through REST endpoints.
"""

from fastapi import FastAPI, HTTPException
from fastapi.middleware.cors import CORSMiddleware
from pydantic import BaseModel
import joblib
import numpy as np
import os
import sys

# Add the parent directory to the path to import from ml folder
sys.path.append(os.path.join(os.path.dirname(__file__), '..'))

# Initialize FastAPI app
app = FastAPI(
    title="Smart Finance Dashboard API",
    description="API for predicting transaction categories using machine learning",
    version="1.0.0"
)

# Add CORS middleware to allow requests from Next.js frontend
app.add_middleware(
    CORSMiddleware,
    allow_origins=["http://localhost:3000", "http://127.0.0.1:3000"],  # Next.js default port
    allow_credentials=True,
    allow_methods=["GET", "POST", "PUT", "DELETE"],
    allow_headers=["*"],
)

# Pydantic model for request body
class PredictionRequest(BaseModel):
    description: str

# Pydantic model for response body
class PredictionResponse(BaseModel):
    description: str
    predicted_category: str
    confidence: float

# Global variables for model and vectorizer
model = None
vectorizer = None

def load_model():
    """Load the trained ML model and vectorizer"""
    global model, vectorizer
    
    try:
        # Path to the ML models folder
        model_path = os.path.join(os.path.dirname(__file__), '..', 'ml', 'models', 'category_model.pkl')
        vectorizer_path = os.path.join(os.path.dirname(__file__), '..', 'ml', 'models', 'tfidf_vectorizer.pkl')
        
        print(f"Loading model from: {model_path}")
        print(f"Loading vectorizer from: {vectorizer_path}")
        
        # Load the trained model and TF-IDF vectorizer
        model = joblib.load(model_path)
        vectorizer = joblib.load(vectorizer_path)
        
        print("Model and vectorizer loaded successfully!")
        
        # Try to load model metadata
        try:
            metadata_path = os.path.join(os.path.dirname(__file__), '..', 'ml', 'models', 'model_metadata.pkl')
            metadata = joblib.load(metadata_path)
            print(f"Model info: {metadata.get('model_name', 'Unknown')} - Accuracy: {metadata.get('accuracy', 'Unknown')}")
        except:
            print("Model metadata not found, continuing without it...")
            
    except FileNotFoundError as e:
        print(f"Error loading model: {e}")
        print("Please make sure the ML model is trained by running train_category_model.py")
        raise e
    except Exception as e:
        print(f"Unexpected error loading model: {e}")
        raise e

def predict_category(description: str):
    """Predict the category for a given transaction description"""
    try:
        # Clean the input description (same as training)
        cleaned_description = description.lower().strip()
        
        # Transform the text using the loaded vectorizer
        description_tfidf = vectorizer.transform([cleaned_description])
        
        # Make prediction
        prediction = model.predict(description_tfidf)[0]
        
        # Get confidence score if available
        confidence = None
        if hasattr(model, 'predict_proba'):
            # For models that support probability predictions
            prediction_proba = model.predict_proba(description_tfidf)
            confidence = float(prediction_proba.max())
        elif hasattr(model, 'decision_function'):
            # For models that support decision function (like LinearSVC)
            decision_scores = model.decision_function(description_tfidf)
            if len(decision_scores.shape) == 1:
                # Binary classification
                confidence = float(abs(decision_scores[0]))
            else:
                # Multi-class classification
                confidence = float(np.max(decision_scores))
                # Normalize to 0-1 range for better interpretation
                confidence = float(1 / (1 + np.exp(-confidence)))
        
        # Ensure confidence is a float and round to 4 decimal places
        if confidence is not None:
            confidence = round(float(confidence), 4)
        else:
            confidence = 0.0  # Default confidence if not available
            
        return prediction, confidence
        
    except Exception as e:
        print(f"Error making prediction: {e}")
        raise e

# Load the model when the application starts
@app.on_event("startup")
async def startup_event():
    """Load the ML model when the FastAPI app starts"""
    load_model()

@app.get("/")
async def root():
    """Root endpoint to check if the API is running"""
    return {
        "message": "Smart Finance Dashboard API is running!",
        "version": "1.0.0",
        "endpoints": {
            "predict": "/predict-category (POST)",
            "docs": "/docs (Swagger UI)",
            "redoc": "/redoc (ReDoc)"
        }
    }

@app.get("/health")
async def health_check():
    """Health check endpoint"""
    if model is None or vectorizer is None:
        raise HTTPException(status_code=503, detail="Model not loaded")
    
    return {
        "status": "healthy",
        "model_loaded": True,
        "api_version": "1.0.0"
    }

@app.post("/predict-category", response_model=PredictionResponse)
async def predict_category_endpoint(request: PredictionRequest):
    """
    Predict the category for a transaction description
    
    Args:
        request: PredictionRequest containing the transaction description
        
    Returns:
        PredictionResponse with predicted category and confidence score
    """
    try:
        # Validate input
        if not request.description or not request.description.strip():
            raise HTTPException(status_code=400, detail="Description cannot be empty")
        
        # Make prediction
        predicted_category, confidence = predict_category(request.description)
        
        # Return response
        return PredictionResponse(
            description=request.description,
            predicted_category=predicted_category,
            confidence=confidence
        )
        
    except Exception as e:
        print(f"Error in prediction endpoint: {e}")
        raise HTTPException(status_code=500, detail=f"Prediction failed: {str(e)}")

@app.get("/categories")
async def get_available_categories():
    """Get list of available transaction categories"""
    # This would ideally come from the model, but for now we'll return the known categories
    categories = ["Food", "Shopping", "Entertainment", "Transport", "Income"]
    return {
        "categories": categories,
        "count": len(categories)
    }

if __name__ == "__main__":
    import uvicorn
    print("Starting FastAPI server...")
    print("Run this command: uvicorn main:app --reload --port 8000")
    print("API will be available at: http://localhost:8000")
    print("Swagger UI will be available at: http://localhost:8000/docs")
