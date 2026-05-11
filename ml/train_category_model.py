"""
Improved Transaction Category Prediction Model Training
This script trains multiple machine learning models to predict transaction categories
based on transaction descriptions and selects the best performing one.
"""

import pandas as pd
import numpy as np
from sklearn.model_selection import train_test_split
from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.linear_model import LogisticRegression
from sklearn.svm import LinearSVC
from sklearn.naive_bayes import MultinomialNB
from sklearn.metrics import accuracy_score, classification_report
import joblib
import os
import warnings

# Suppress warnings for cleaner output
warnings.filterwarnings('ignore')

def load_and_clean_data():
    """Load and clean the transaction dataset"""
    print("Loading and cleaning data...")
    
    # Load the dataset
    df = pd.read_csv("data/transactions_with_category.csv")
    
    # Display basic info about the dataset
    print(f"Dataset shape: {df.shape}")
    print(f"Categories: {df['category'].unique()}")
    print(f"Category distribution:")
    print(df['category'].value_counts())
    
    # Clean the data
    # Remove rows with null values in description or category
    df = df.dropna(subset=['description', 'category'])
    
    # Clean descriptions: lowercase and remove extra spaces
    df['description_cleaned'] = df['description'].str.lower().str.strip()
    
    # Remove any remaining null values
    df = df.dropna()
    
    print(f"Cleaned dataset shape: {df.shape}")
    return df

def train_multiple_models(df):
    """Train multiple models and compare their performance"""
    print("\nTraining multiple models...")
    
    # Prepare features (X) and target (y)
    X = df['description_cleaned']  # Transaction descriptions
    y = df['category']  # Transaction categories
    
    # Split the data into training and testing sets
    X_train, X_test, y_train, y_test = train_test_split(
        X, y, test_size=0.2, random_state=42, stratify=y
    )
    
    print(f"Training set size: {len(X_train)}")
    print(f"Testing set size: {len(X_test)}")
    
    # Create the TF-IDF vectorizer (same for all models)
    vectorizer = TfidfVectorizer(
        max_features=3000,  # Increased features for better performance
        ngram_range=(1, 3),  # Use single words, word pairs, and triplets
        stop_words='english',  # Remove common English words
        min_df=1,  # Include terms that appear in at least 1 document
        max_df=0.9,  # Ignore terms that appear in more than 90% of documents
        sublinear_tf=True,  # Apply sublinear TF scaling
        norm='l2'  # Apply L2 normalization
    )
    
    # Transform the text data
    X_train_tfidf = vectorizer.fit_transform(X_train)
    X_test_tfidf = vectorizer.transform(X_test)
    
    # Define models to test with different hyperparameters
    models = {
        'Logistic Regression': LogisticRegression(
            random_state=42,
            max_iter=2000,
            C=10.0,  # Higher C for less regularization
            solver='liblinear',
            penalty='l2'
        ),
        'Linear SVC': LinearSVC(
            random_state=42,
            max_iter=2000,
            C=10.0,  # Higher C for less regularization
            penalty='l2',
            loss='squared_hinge'
        ),
        'Multinomial NB': MultinomialNB(
            alpha=0.1  # Lower alpha for less smoothing
        )
    }
    
    # Train and evaluate each model
    results = {}
    best_model = None
    best_accuracy = 0
    best_model_name = ""
    
    for name, model in models.items():
        print(f"\n--- Training {name} ---")
        
        # Train the model
        model.fit(X_train_tfidf, y_train)
        
        # Make predictions
        y_pred = model.predict(X_test_tfidf)
        
        # Calculate accuracy
        accuracy = accuracy_score(y_test, y_pred)
        results[name] = {
            'model': model,
            'accuracy': accuracy,
            'predictions': y_pred
        }
        
        print(f"Accuracy: {accuracy:.4f}")
        
        # Check if this is the best model so far
        if accuracy > best_accuracy:
            best_accuracy = accuracy
            best_model = model
            best_model_name = name
    
    # Print detailed results for the best model
    print(f"\n=== BEST MODEL: {best_model_name} ===")
    print(f"Best Accuracy: {best_accuracy:.4f}")
    
    best_predictions = results[best_model_name]['predictions']
    print("\nClassification Report:")
    print(classification_report(y_test, best_predictions))
    
    # Print comparison of all models
    print("\n=== Model Comparison ===")
    for name, result in results.items():
        status = "🏆 BEST" if name == best_model_name else ""
        print(f"{name}: {result['accuracy']:.4f} {status}")
    
    return vectorizer, best_model, best_model_name, best_accuracy

def save_model(vectorizer, model, model_name, accuracy):
    """Save the trained model and vectorizer"""
    print(f"\nSaving {model_name} model...")
    
    # Create models directory if it doesn't exist
    os.makedirs('models', exist_ok=True)
    
    # Save the vectorizer
    joblib.dump(vectorizer, 'models/tfidf_vectorizer.pkl')
    
    # Save the trained model
    joblib.dump(model, 'models/category_model.pkl')
    
    # Save model metadata
    metadata = {
        'model_name': model_name,
        'accuracy': accuracy,
        'feature_count': vectorizer.get_feature_names_out().shape[0]
    }
    joblib.dump(metadata, 'models/model_metadata.pkl')
    
    print("Model saved successfully!")
    print(f"- Vectorizer: models/tfidf_vectorizer.pkl")
    print(f"- Model: models/category_model.pkl")
    print(f"- Metadata: models/model_metadata.pkl")

def main():
    """Main function to run the training pipeline"""
    print("=== Improved Transaction Category Model Training ===")
    
    # Step 1: Load and clean data
    df = load_and_clean_data()
    
    # Step 2: Train multiple models and select the best
    vectorizer, best_model, best_model_name, best_accuracy = train_multiple_models(df)
    
    # Step 3: Save the best model
    save_model(vectorizer, best_model, best_model_name, best_accuracy)
    
    # Step 4: Check if accuracy meets the threshold
    if best_accuracy >= 0.80:
        print(f"\n🎉 SUCCESS! Model achieved {best_accuracy:.4f} accuracy (>= 80%)")
    else:
        print(f"\n⚠️  Model achieved {best_accuracy:.4f} accuracy (< 80%)")
        print("Consider adding more diverse training data to improve performance.")
    
    print("\n=== Training Complete ===")

if __name__ == "__main__":
    main()
