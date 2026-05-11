# Smart Finance Dashboard API Backend

FastAPI backend for the Smart Finance Dashboard ML model that provides REST endpoints for transaction category prediction.

## Project Structure

```
backend/
├── main.py              # FastAPI application with ML model integration
├── requirements.txt     # Python dependencies
├── test_api.py         # API testing script
└── README.md           # This file
```

## Features

- **FastAPI Framework**: Modern, fast web framework for building APIs
- **ML Model Integration**: Loads and uses the trained transaction category model
- **CORS Support**: Configured to work with Next.js frontend
- **Auto Documentation**: Swagger UI and ReDoc documentation
- **Error Handling**: Comprehensive error handling and validation
- **Health Checks**: Endpoint to monitor API and model status

## Installation

1. Install dependencies:
```bash
pip install -r requirements.txt
```

2. Make sure the ML model is trained:
```bash
cd ../ml
python train_category_model.py
```

## Running the API

Start the FastAPI server:

```bash
uvicorn main:app --reload --port 8000
```

The API will be available at:
- **API Base URL**: http://localhost:8000
- **Swagger UI**: http://localhost:8000/docs
- **ReDoc**: http://localhost:8000/redoc

## API Endpoints

### 1. Root Endpoint
```
GET /
```
Returns API information and available endpoints.

### 2. Health Check
```
GET /health
```
Returns the health status of the API and ML model.

**Response:**
```json
{
  "status": "healthy",
  "model_loaded": true,
  "api_version": "1.0.0"
}
```

### 3. Get Categories
```
GET /categories
```
Returns the list of available transaction categories.

**Response:**
```json
{
  "categories": ["Food", "Shopping", "Entertainment", "Transport", "Income"],
  "count": 5
}
```

### 4. Predict Category
```
POST /predict-category
```
Predicts the category for a given transaction description.

**Request Body:**
```json
{
  "description": "Grab Food"
}
```

**Response:**
```json
{
  "description": "Grab Food",
  "predicted_category": "Food",
  "confidence": 0.7146
}
```

## Testing

Run the test script to verify all endpoints:

```bash
python test_api.py
```

This will test:
- Health check endpoint
- Root endpoint
- Categories endpoint
- Prediction endpoint with multiple test cases
- Error handling for invalid inputs

## Example API Calls

### Using curl

```bash
# Health check
curl -X GET "http://localhost:8000/health"

# Get categories
curl -X GET "http://localhost:8000/categories"

# Predict category
curl -X POST "http://localhost:8000/predict-category" \
  -H "Content-Type: application/json" \
  -d '{"description": "Grab Food"}'
```

### Using JavaScript (Frontend)

```javascript
// Predict category
const response = await fetch('http://localhost:8000/predict-category', {
  method: 'POST',
  headers: {
    'Content-Type': 'application/json',
  },
  body: JSON.stringify({
    description: 'Grab Food'
  })
});

const result = await response.json();
console.log(result);
// Output: { description: "Grab Food", predicted_category: "Food", confidence: 0.7146 }
```

### Using Python

```python
import requests

# Predict category
response = requests.post(
    'http://localhost:8000/predict-category',
    json={'description': 'Grab Food'}
)

result = response.json()
print(result)
# Output: {'description': 'Grab Food', 'predicted_category': 'Food', 'confidence': 0.7146}
```

## Model Integration

The API automatically loads the trained ML model from:
- `../ml/models/category_model.pkl` (trained model)
- `../ml/models/tfidf_vectorizer.pkl` (text vectorizer)
- `../ml/models/model_metadata.pkl` (model metadata)

The model is loaded when the application starts and is ready for predictions immediately.

## CORS Configuration

The API is configured to accept requests from:
- `http://localhost:3000` (Next.js default)
- `http://127.0.0.1:3000`

You can modify the CORS settings in `main.py` if your frontend runs on a different port.

## Error Handling

The API includes comprehensive error handling:

- **400 Bad Request**: Invalid input (empty description)
- **500 Internal Server Error**: Model prediction failures
- **503 Service Unavailable**: Model not loaded

## Development

### Adding New Endpoints

1. Define Pydantic models for request/response if needed
2. Create the endpoint function with proper error handling
3. Add appropriate type hints and documentation
4. Test the new endpoint

### Model Updates

When you retrain the ML model:
1. Run `train_category_model.py` in the ml folder
2. Restart the FastAPI server (it will automatically load the new model)
3. Test the updated predictions

## Production Considerations

For production deployment:

1. **Environment Variables**: Use environment variables for model paths and configuration
2. **Logging**: Add structured logging for monitoring
3. **Rate Limiting**: Implement rate limiting to prevent abuse
4. **Authentication**: Add API key or JWT authentication
5. **Scaling**: Consider using multiple workers with Gunicorn
6. **Monitoring**: Add health checks and monitoring endpoints

## Troubleshooting

### Model Not Loading
- Ensure the ML model is trained: `cd ../ml && python train_category_model.py`
- Check file paths in `main.py`
- Verify model files exist in `../ml/models/`

### CORS Issues
- Check that your frontend URL is in the CORS allow_origins list
- Verify the frontend is making requests with the correct headers

### Prediction Errors
- Check the server logs for detailed error messages
- Ensure the input description is not empty
- Verify the model is loaded (check `/health` endpoint)
