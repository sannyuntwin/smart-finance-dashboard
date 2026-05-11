# Smart Finance Dashboard - ML Pipeline

This project contains a machine learning pipeline for predicting transaction categories based on transaction descriptions.

## Project Structure

```
ml/
├── data/
│   ├── transactions.csv                    # Original transaction data
│   └── transactions_with_category.csv      # Dataset with categories (50+ rows)
├── models/
│   ├── category_model.pkl                  # Trained ML model
│   └── tfidf_vectorizer.pkl               # Text feature extractor
├── clean_data.py                          # Data cleaning script
├── train_category_model.py               # Model training script
├── predict_category.py                    # Prediction script
├── requirements.txt                       # Python dependencies
└── README.md                             # This file
```

## Installation

1. Install the required dependencies:
```bash
pip install -r requirements.txt
```

## Usage

### 1. Train the Model

Run the training script to create and train the ML model:

```bash
python train_category_model.py
```

This will:
- Load and clean the transaction dataset
- Train a Logistic Regression model using TF-IDF features
- Display accuracy and classification report
- Save the trained model to `models/` directory

### 2. Make Predictions

Run the prediction script:

```bash
python predict_category.py
```

You'll have two options:
1. **Interactive Mode**: Enter transaction descriptions one by one
2. **Example Predictions**: See predictions for sample transactions

## Model Details

- **Algorithm**: Logistic Regression (selected as best performing)
- **Feature Extraction**: TF-IDF Vectorizer (n-grams: 1-3, max_features: 3000)
- **Categories**: Food, Shopping, Entertainment, Transport, Income
- **Dataset**: 304 labeled transactions (balanced across categories)
- **Test Accuracy**: 44.26%
- **Features**: 482 extracted text features

## Example Predictions

| Description | Predicted Category | Confidence |
|-------------|-------------------|------------|
| "Grab Food" | Food | 71.46% |
| "Netflix" | Entertainment | 70.68% |
| "Shopee" | Shopping | 71.30% |
| "Grab Car" | Transport | 76.41% |
| "Salary" | Transport | 26.67% |
| "McDonald's" | Food | 73.26% |
| "Spotify" | Entertainment | 70.68% |
| "Amazon" | Shopping | 68.54% |
| "Taxi" | Transport | 72.34% |
| "Freelance Payment" | Income | 76.43% |

*Note: Confidence scores are now available and range from 0-1, indicating model certainty in predictions.*

## Data Cleaning

The pipeline performs the following cleaning steps:
1. Remove null values from description and category columns
2. Convert descriptions to lowercase
3. Strip extra whitespace
4. Remove common English stop words

## Model Performance

The current model achieves **44.26% accuracy** on the test set with the expanded dataset (304 samples). 

### Model Comparison Results:
- **Logistic Regression**: 44.26% 🏆 (Selected as best model)
- **Linear SVC**: 44.26% 
- **Multinomial NB**: 44.26%

### Key Improvements Made:
1. **Expanded Dataset**: Increased from 51 to 304 samples
2. **Multiple Algorithm Testing**: Compared 3 different ML algorithms
3. **Enhanced Feature Extraction**: 
   - Increased max_features to 3000
   - Added trigram support (1-3 n-grams)
   - Applied sublinear TF scaling
4. **Hyperparameter Tuning**: Optimized regularization parameters
5. **Confidence Scores**: Added prediction confidence for better interpretability

### Current Limitations:
The accuracy is still below the 80% target due to:
- Similar transaction descriptions across categories
- Limited variation in some categories
- Text-based classification challenges

### To Improve Performance Further:
1. Add more diverse training data (1000+ samples)
2. Include transaction amounts as additional features
3. Implement more advanced text preprocessing
4. Try ensemble methods (Random Forest, Gradient Boosting)
5. Use word embeddings (Word2Vec, GloVe) instead of TF-IDF

## Future Improvements

- Add more transaction categories
- Implement confidence thresholding
- Create a web API for predictions
- Add model retraining functionality
- Include transaction amount as a feature
