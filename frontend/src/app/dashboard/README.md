# Finance Dashboard

A comprehensive CSV upload and analysis dashboard for transaction categorization using machine learning.

## Features

### 📊 **CSV Upload & Processing**
- Drag-and-drop CSV file upload
- Automatic CSV parsing with validation
- Real-time progress tracking during processing
- Error handling for invalid files

### 🤖 **Machine Learning Integration**
- Automatic category prediction for each transaction
- Confidence scoring for predictions
- Batch processing of multiple transactions
- Integration with FastAPI ML backend

### 📈 **Data Visualization**
- **Summary Cards**: Total income, expenses, balance, transaction count
- **Pie Chart**: Expense breakdown by category
- **Bar Chart**: Income vs Expense comparison
- **Responsive Charts**: Built with Recharts library

### 📋 **Transaction Table**
- Detailed view of all transactions
- Color-coded amounts (green for income, red for expenses)
- Category badges with confidence scores
- Pagination for large datasets

## CSV Format Requirements

The dashboard expects CSV files with the following columns:

```csv
date,description,amount,type
2024-01-01,Grab Food,15.50,expense
2024-01-02,Netflix Subscription,12.99,expense
2024-01-03,Monthly Salary,3500.00,income
```

### Column Specifications:
- **date**: Transaction date (any format)
- **description**: Transaction description (used for ML prediction)
- **amount**: Numeric amount (positive values only)
- **type**: Transaction type ("income" or "expense")

## Usage Instructions

### 1. **Upload CSV File**
- Click "Click to upload CSV file" or drag and drop
- Select a CSV file with the required columns
- Wait for processing to complete

### 2. **View Results**
- **Summary Cards**: Overview of financial metrics
- **Charts**: Visual analysis of spending patterns
- **Transaction Table**: Detailed transaction breakdown

### 3. **Analyze Data**
- Review predicted categories and confidence scores
- Identify spending patterns by category
- Monitor income vs expense balance

## Technical Implementation

### **State Management**
```typescript
const [transactions, setTransactions] = useState<Transaction[]>([]);
const [stats, setStats] = useState<DashboardStats>({
  totalIncome: 0,
  totalExpense: 0,
  balance: 0,
  totalTransactions: 0
});
```

### **CSV Processing**
- Uses PapaParse for robust CSV parsing
- Validates required columns and data types
- Handles parsing errors gracefully

### **ML Integration**
```typescript
const predictCategory = async (description: string) => {
  const response = await fetch('http://localhost:8000/predict-category', {
    method: 'POST',
    headers: { 'Content-Type': 'application/json' },
    body: JSON.stringify({ description })
  });
  return response.json();
};
```

### **Data Visualization**
- **Recharts**: Professional charting library
- **Responsive Design**: Charts adapt to screen size
- **Color Coding**: Consistent color scheme throughout

## Error Handling

### **CSV Validation**
- Missing required columns
- Invalid data formats
- Empty files
- Corrupted CSV structure

### **API Errors**
- Network connectivity issues
- Backend service unavailable
- Invalid API responses
- Prediction failures

### **User Feedback**
- Progress indicators during processing
- Clear error messages
- Loading states
- Success confirmations

## Performance Considerations

### **Large File Handling**
- Processes transactions in batches
- Progress tracking for user feedback
- Memory-efficient parsing
- Pagination for large datasets

### **API Optimization**
- Sequential processing to prevent overload
- Error recovery for individual transactions
- Timeout handling
- Retry logic for failed requests

## Sample Data

A sample CSV file is provided at:
```
d:\smart-finance-dashboard\sample_transactions.csv
```

This includes 20 sample transactions with various categories for testing.

## Styling & Design

### **UI Components**
- **Tailwind CSS**: Utility-first styling
- **Responsive Design**: Mobile-first approach
- **Color Scheme**: Professional blue/green palette
- **Animations**: Smooth transitions and micro-interactions

### **Visual Hierarchy**
- Clear section separation
- Consistent spacing and typography
- Intuitive navigation
- Accessible color contrasts

## Future Enhancements

### **Planned Features**
- Export functionality (PDF/Excel)
- Transaction filtering and search
- Date range selection
- Custom categories
- Transaction editing
- Data persistence
- User accounts

### **Advanced Analytics**
- Trend analysis over time
- Spending forecasts
- Budget tracking
- Savings goals
- Category comparisons

## Troubleshooting

### **Common Issues**

1. **CSV Upload Fails**
   - Check file format (must be .csv)
   - Verify required columns exist
   - Ensure data types are correct

2. **Predictions Not Working**
   - Confirm FastAPI backend is running
   - Check network connectivity
   - Verify API endpoint accessibility

3. **Charts Not Displaying**
   - Ensure transactions have valid data
   - Check for JavaScript errors
   - Verify Recharts installation

4. **Performance Issues**
   - Large files may take time to process
   - Consider splitting large CSV files
   - Check browser memory usage

### **Debug Mode**
Enable browser developer tools to:
- Monitor network requests
- Check console for errors
- Inspect component state
- Profile performance

## Dependencies

```json
{
  "papaparse": "^5.4.1",
  "@types/papaparse": "^5.3.14", 
  "recharts": "^2.12.7"
}
```

## Browser Support

- Chrome 90+
- Firefox 88+
- Safari 14+
- Edge 90+

## File Size Limits

- **Recommended**: Up to 1,000 transactions per CSV
- **Maximum**: 5,000 transactions (performance may degrade)
- **Processing Time**: ~1 second per 100 transactions
