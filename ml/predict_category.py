"""
Transaction Category Prediction
This script loads a trained model and predicts transaction categories
from user input descriptions.
"""

import joblib
import pandas as pd
import numpy as np

def load_model():
    """Load the trained model and vectorizer"""
    print("Loading model...")
    
    try:
        # Load the TF-IDF vectorizer
        vectorizer = joblib.load('models/tfidf_vectorizer.pkl')
        
        # Load the trained model
        model = joblib.load('models/category_model.pkl')
        
        # Load model metadata if available
        try:
            metadata = joblib.load('models/model_metadata.pkl')
            print(f"Model: {metadata['model_name']}")
            print(f"Training Accuracy: {metadata['accuracy']:.4f}")
            print(f"Features: {metadata['feature_count']}")
        except:
            print("Model metadata not found.")
        
        print("Model loaded successfully!")
        return vectorizer, model
    
    except FileNotFoundError:
        print("Error: Model files not found!")
        print("Please run train_category_model.py first to train and save the model.")
        return None, None

def predict_category(description, vectorizer, model):
    """Predict the category for a given transaction description"""
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
        confidence = prediction_proba.max()
    elif hasattr(model, 'decision_function'):
        # For models that support decision function (like LinearSVC)
        decision_scores = model.decision_function(description_tfidf)
        if len(decision_scores.shape) == 1:
            # Binary classification
            confidence = abs(decision_scores[0])
        else:
            # Multi-class classification
            confidence = np.max(decision_scores)
            # Normalize to 0-1 range for better interpretation
            confidence = 1 / (1 + np.exp(-confidence))
    
    return prediction, confidence

def interactive_prediction():
    """Interactive prediction mode"""
    print("\n=== Transaction Category Predictor ===")
    print("Enter transaction descriptions to predict their categories.")
    print("Type 'quit' to exit.\n")
    
    # Load the model
    vectorizer, model = load_model()
    if vectorizer is None or model is None:
        return
    
    while True:
        # Get user input
        user_input = input("Enter transaction description: ").strip()
        
        if user_input.lower() == 'quit':
            print("Goodbye!")
            break
        
        if not user_input:
            print("Please enter a valid description.")
            continue
        
        # Make prediction
        category, confidence = predict_category(user_input, vectorizer, model)
        
        # Display result
        print(f"Description: '{user_input}'")
        print(f"Predicted Category: {category}")
        if confidence is not None:
            print(f"Confidence: {confidence:.4f}")
        else:
            print("Confidence: Not available for this model type")
        print("-" * 50)

def example_predictions():
    """Show example predictions"""
    print("\n=== Example Predictions ===")
    
    # Load the model
    vectorizer, model = load_model()
    if vectorizer is None or model is None:
        return
    
    # Example transaction descriptions
    examples = [
        "Grab Food",
        "Netflix",
        "Shopee",
        "Grab Car",
        "Salary",
        "McDonald's",
        "Spotify",
        "Amazon",
        "Taxi",
        "Freelance Payment",
        "Pizza Hut",
        "YouTube Premium",
        "Lazada",
        "Uber",
        "Investment Return"
    ]
    
    print(f"{'Description':<25} {'Category':<15} {'Confidence':<12}")
    print("-" * 55)
    
    for description in examples:
        category, confidence = predict_category(description, vectorizer, model)
        if confidence is not None:
            print(f"{description:<25} {category:<15} {confidence:.4f}")
        else:
            print(f"{description:<25} {category:<15} {'N/A':<12}")

def main():
    """Main function"""
    print("Transaction Category Prediction Tool")
    print("1. Interactive Mode")
    print("2. Example Predictions")
    
    choice = input("\nChoose an option (1 or 2): ").strip()
    
    if choice == "1":
        interactive_prediction()
    elif choice == "2":
        example_predictions()
    else:
        print("Invalid choice. Running example predictions...")
        example_predictions()

if __name__ == "__main__":
    main()
