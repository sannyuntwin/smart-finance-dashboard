# Smart Finance Dashboard 🏦

A comprehensive full-stack financial dashboard that uses machine learning to automatically categorize transactions from CSV files. Built with Next.js, FastAPI, and Scikit-learn.

## 🌟 Features

### 🤖 **Machine Learning Powered**
- Automatic transaction categorization using NLP
- Confidence scoring for predictions
- 5 categories: Food, Shopping, Entertainment, Transport, Income
- 44.26% accuracy with 304 training samples

### 📊 **Interactive Dashboard**
- CSV file upload with drag-and-drop interface
- Real-time transaction processing
- Financial summary cards (income, expenses, balance)
- Interactive charts (pie charts, bar charts)
- Detailed transaction table with ML predictions

### 🎯 **Single Transaction Prediction**
- Instant category prediction for individual transactions
- Real-time confidence scores
- Clean, responsive UI

### 🏗️ **Modern Tech Stack**
- **Frontend**: Next.js 14, TypeScript, Tailwind CSS, Recharts
- **Backend**: FastAPI, Python, Uvicorn
- **ML**: Scikit-learn, Pandas, NumPy, Joblib
- **Data Processing**: PapaParse for CSV handling

## 🚀 Quick Start

### Prerequisites
- Node.js 18+ 
- Python 3.8+
- Git

### 1. **Clone the Repository**
```bash
git clone <your-repo-url>
cd smart-finance-dashboard
```

### 2. **Setup Backend (FastAPI + ML)**
```bash
cd backend
pip install -r requirements.txt

# Train the ML model (first time only)
cd ../ml
python train_category_model.py

# Start the API server
cd ../backend
uvicorn main:app --reload --port 8000
```

### 3. **Setup Frontend (Next.js)**
```bash
cd frontend
npm install
npm run dev
```

### 4. **Access the Application**
- **Frontend**: http://localhost:3000
- **API Documentation**: http://localhost:8000/docs
- **Dashboard**: http://localhost:3000/dashboard
- **Prediction Tool**: http://localhost:3000/predict

## 📁 Project Structure

```
smart-finance-dashboard/
├── backend/                    # FastAPI API server
│   ├── main.py                # FastAPI application
│   ├── requirements.txt       # Python dependencies
│   ├── test_api.py           # API testing script
│   └── demo.py               # API demo script
├── frontend/                  # Next.js frontend
│   ├── src/
│   │   └── app/
│   │       ├── dashboard/     # CSV upload dashboard
│   │       ├── predict/       # Single prediction page
│   │       └── page.tsx       # Landing page
│   └── package.json          # Node.js dependencies
├── ml/                        # Machine learning pipeline
│   ├── data/                 # Training data
│   ├── models/               # Trained models
│   ├── train_category_model.py  # Training script
│   └── predict_category.py   # Prediction script
├── sample_transactions.csv    # Sample CSV for testing
└── README.md                  # This file
```

## 🎯 Usage Guide

### **Single Transaction Prediction**
1. Go to http://localhost:3000/predict
2. Enter a transaction description (e.g., "Grab Food")
3. Click "Predict Category"
4. View the prediction with confidence score

### **CSV Dashboard Analysis**
1. Go to http://localhost:3000/dashboard
2. Upload a CSV file with columns: `date,description,amount,type`
3. Wait for ML processing (shows progress)
4. Analyze the results:
   - Summary cards showing financial overview
   - Charts for spending patterns
   - Detailed transaction table with predictions

### **Sample CSV Format**
```csv
date,description,amount,type
2024-01-01,Grab Food,15.50,expense
2024-01-02,Netflix Subscription,12.99,expense
2024-01-03,Monthly Salary,3500.00,income
```

## 🤖 Machine Learning Model

### **Model Details**
- **Algorithm**: Logistic Regression (best performing)
- **Features**: TF-IDF vectorization with trigrams
- **Training Data**: 304 labeled transactions
- **Accuracy**: 44.26% on test set
- **Categories**: Food, Shopping, Entertainment, Transport, Income

### **Model Training**
```bash
cd ml
python train_category_model.py
```

The training script:
1. Loads and cleans transaction data
2. Tests multiple algorithms (Logistic Regression, LinearSVC, Naive Bayes)
3. Selects the best performing model
4. Saves model and vectorizer for API use

### **Prediction API**
```bash
curl -X POST "http://localhost:8000/predict-category" \
  -H "Content-Type: application/json" \
  -d '{"description": "Grab Food"}'
```

**Response:**
```json
{
  "description": "Grab Food",
  "predicted_category": "Food",
  "confidence": 0.7146
}
```

## 🛠️ Development

### **Frontend Development**
```bash
cd frontend
npm run dev          # Start development server
npm run build        # Build for production
npm run start        # Start production server
```

### **Backend Development**
```bash
cd backend
uvicorn main:app --reload --port 8000  # Start development server
python test_api.py                      # Test API endpoints
python demo.py                          # Run API demo
```

### **ML Model Development**
```bash
cd ml
python train_category_model.py  # Retrain model with new data
python predict_category.py      # Test predictions manually
```

## 📊 API Endpoints

### **FastAPI Backend (http://localhost:8000)**

| Method | Endpoint | Description |
|--------|----------|-------------|
| GET | `/` | API information |
| GET | `/health` | Health check |
| GET | `/categories` | List available categories |
| POST | `/predict-category` | Predict transaction category |

### **API Documentation**
- **Swagger UI**: http://localhost:8000/docs
- **ReDoc**: http://localhost:8000/redoc

## 🎨 Frontend Pages

### **Landing Page (`/`)**
- Introduction to the Smart Finance Dashboard
- Feature highlights and technology stack
- Navigation to prediction tool and dashboard

### **Prediction Page (`/predict`)**
- Single transaction prediction interface
- Real-time ML predictions with confidence scores
- Clean, responsive form design

### **Dashboard Page (`/dashboard`)**
- CSV upload interface with drag-and-drop
- Financial summary cards and charts
- Detailed transaction analysis table
- Batch ML processing with progress tracking

## 🔧 Configuration

### **Environment Variables**
Create `.env.local` in frontend directory:
```env
NEXT_PUBLIC_API_URL=http://localhost:8000
```

### **CORS Configuration**
Backend is configured to accept requests from:
- `http://localhost:3000`
- `http://127.0.0.1:3000`

## 📈 Performance

### **Model Performance**
- **Training Time**: ~2 seconds
- **Prediction Time**: ~50ms per transaction
- **Memory Usage**: ~50MB for model and vectorizer
- **Accuracy**: 44.26% (can be improved with more data)

### **Application Performance**
- **Frontend**: Next.js with optimized builds
- **Backend**: FastAPI with async processing
- **CSV Processing**: Handles up to 1000 transactions efficiently
- **Charts**: Responsive and performant with Recharts

## 🚀 Deployment

### **Frontend Deployment (Vercel)**
```bash
cd frontend
npm run build
# Deploy to Vercel or any Next.js hosting
```

### **Backend Deployment (Heroku/Railway)**
```bash
cd backend
# Deploy to any Python hosting service
# Ensure model files are included in deployment
```

### **Environment Setup for Production**
1. Set production API URL in frontend
2. Configure CORS for production domain
3. Ensure model files are deployed with backend
4. Set up proper environment variables

## 🔮 Future Enhancements

### **Model Improvements**
- [ ] Expand training dataset to 1000+ samples
- [ ] Add transaction amounts as features
- [ ] Try advanced algorithms (Random Forest, XGBoost)
- [ ] Implement word embeddings instead of TF-IDF
- [ ] Target 80%+ accuracy

### **Feature Enhancements**
- [ ] User authentication and accounts
- [ ] Transaction history persistence
- [ ] Advanced filtering and search
- [ ] Export functionality (PDF/Excel)
- [ ] Budget tracking and goals
- [ ] Mobile app (React Native)

### **Technical Improvements**
- [ ] Database integration (PostgreSQL/MongoDB)
- [ ] Redis caching for predictions
- [ ] Microservices architecture
- [ ] Real-time updates with WebSockets
- [ ] Advanced analytics and reporting

## 🐛 Troubleshooting

### **Common Issues**

1. **Model Not Loading**
   ```bash
   cd ml && python train_category_model.py
   ```

2. **API Connection Error**
   - Ensure backend is running on port 8000
   - Check CORS configuration
   - Verify network connectivity

3. **CSV Upload Fails**
   - Check CSV format (required columns: date,description,amount,type)
   - Ensure file is properly formatted
   - Check file size (recommended < 1000 transactions)

4. **Frontend Build Errors**
   ```bash
   cd frontend && npm install
   npm run build
   ```

### **Debug Mode**
- **Frontend**: Check browser developer tools
- **Backend**: Check terminal logs and API docs
- **ML**: Run prediction script manually

## 📄 License

This project is open source and available under the [MIT License](LICENSE).

## 🤝 Contributing

Contributions are welcome! Please feel free to submit a Pull Request.

1. Fork the repository
2. Create a feature branch
3. Make your changes
4. Add tests if applicable
5. Submit a pull request

## 📞 Support

If you have any questions or issues, please:
1. Check the troubleshooting section
2. Review the API documentation
3. Open an issue on GitHub

---

**Built with ❤️ using Next.js, FastAPI, and Machine Learning**
