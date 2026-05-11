"use client";

import React, { useState } from 'react';

// TypeScript interface for API request
interface PredictionRequest {
  description: string;
}

// TypeScript interface for API response
interface PredictionResponse {
  description: string;
  predicted_category: string;
  confidence: number;
}

// TypeScript interface for component state
interface PredictionState {
  description: string;
  result: PredictionResponse | null;
  loading: boolean;
  error: string | null;
}

export default function PredictPage() {
  // State management for the prediction form
  const [state, setState] = useState<PredictionState>({
    description: '',
    result: null,
    loading: false,
    error: null,
  });

  // Function to handle API call to FastAPI backend
  const predictCategory = async () => {
    // Reset previous results and errors
    setState(prev => ({ ...prev, loading: true, error: null, result: null }));

    try {
      // Validate input
      if (!state.description.trim()) {
        setState(prev => ({ 
          ...prev, 
          loading: false, 
          error: 'Please enter a transaction description' 
        }));
        return;
      }

      // Make API request to FastAPI backend
      const response = await fetch('http://localhost:8000/predict-category', {
        method: 'POST',
        headers: {
          'Content-Type': 'application/json',
        },
        body: JSON.stringify({
          description: state.description.trim()
        } as PredictionRequest),
      });

      // Handle API errors
      if (!response.ok) {
        const errorData = await response.json().catch(() => ({}));
        throw new Error(errorData.detail || `HTTP ${response.status}: ${response.statusText}`);
      }

      // Parse successful response
      const data: PredictionResponse = await response.json();
      
      // Update state with prediction result
      setState(prev => ({
        ...prev,
        result: data,
        loading: false,
      }));

    } catch (error) {
      // Handle network or parsing errors
      console.error('Prediction error:', error);
      setState(prev => ({
        ...prev,
        loading: false,
        error: error instanceof Error ? error.message : 'An unexpected error occurred'
      }));
    }
  };

  // Handle form submission
  const handleSubmit = (e: React.FormEvent) => {
    e.preventDefault();
    predictCategory();
  };

  // Handle input change
  const handleInputChange = (e: React.ChangeEvent<HTMLInputElement>) => {
    setState(prev => ({ 
      ...prev, 
      description: e.target.value,
      error: null // Clear error when user starts typing
    }));
  };

  // Handle Enter key press
  const handleKeyPress = (e: React.KeyboardEvent<HTMLInputElement>) => {
    if (e.key === 'Enter') {
      handleSubmit(e);
    }
  };

  // Get confidence color based on score
  const getConfidenceColor = (confidence: number): string => {
    if (confidence >= 0.8) return 'text-green-600';
    if (confidence >= 0.6) return 'text-yellow-600';
    return 'text-red-600';
  };

  // Get confidence badge color
  const getConfidenceBadgeColor = (confidence: number): string => {
    if (confidence >= 0.8) return 'bg-green-100 text-green-800 border-green-200';
    if (confidence >= 0.6) return 'bg-yellow-100 text-yellow-800 border-yellow-200';
    return 'bg-red-100 text-red-800 border-red-200';
  };

  return (
    <div className="min-h-screen bg-gradient-to-br from-blue-50 to-indigo-100">
      <div className="container mx-auto px-4 py-8">
        {/* Header */}
        <div className="text-center mb-12">
          <h1 className="text-4xl font-bold text-gray-800 mb-4">
            Transaction Category Predictor
          </h1>
          <p className="text-lg text-gray-600 max-w-2xl mx-auto">
            Use machine learning to automatically categorize your transactions based on their descriptions.
          </p>
        </div>

        {/* Main Content */}
        <div className="max-w-2xl mx-auto">
          {/* Input Form */}
          <div className="bg-white rounded-2xl shadow-xl p-8 mb-8">
            <form onSubmit={handleSubmit} className="space-y-6">
              {/* Input Field */}
              <div>
                <label htmlFor="description" className="block text-sm font-medium text-gray-700 mb-2">
                  Transaction Description
                </label>
                <input
                  type="text"
                  id="description"
                  value={state.description}
                  onChange={handleInputChange}
                  onKeyPress={handleKeyPress}
                  placeholder="e.g., Grab Food, Netflix, Shopee, Salary"
                  className="w-full px-4 py-3 border border-gray-300 rounded-lg focus:ring-2 focus:ring-blue-500 focus:border-transparent outline-none transition-all duration-200"
                  disabled={state.loading}
                />
                <p className="mt-2 text-sm text-gray-500">
                  Enter a transaction description to predict its category
                </p>
              </div>

              {/* Error Message */}
              {state.error && (
                <div className="bg-red-50 border border-red-200 rounded-lg p-4">
                  <div className="flex items-center">
                    <svg className="w-5 h-5 text-red-400 mr-2" fill="currentColor" viewBox="0 0 20 20">
                      <path fillRule="evenodd" d="M10 18a8 8 0 100-16 8 8 0 000 16zM8.707 7.293a1 1 0 00-1.414 1.414L8.586 10l-1.293 1.293a1 1 0 101.414 1.414L10 11.414l1.293 1.293a1 1 0 001.414-1.414L11.414 10l1.293-1.293a1 1 0 00-1.414-1.414L10 8.586 8.707 7.293z" clipRule="evenodd" />
                    </svg>
                    <span className="text-red-700 text-sm">{state.error}</span>
                  </div>
                </div>
              )}

              {/* Submit Button */}
              <button
                type="submit"
                disabled={state.loading || !state.description.trim()}
                className="w-full bg-blue-600 text-white py-3 px-6 rounded-lg font-medium hover:bg-blue-700 focus:ring-4 focus:ring-blue-500 focus:ring-opacity-50 disabled:opacity-50 disabled:cursor-not-allowed transition-all duration-200 flex items-center justify-center"
              >
                {state.loading ? (
                  <>
                    <svg className="animate-spin -ml-1 mr-3 h-5 w-5 text-white" fill="none" viewBox="0 0 24 24">
                      <circle className="opacity-25" cx="12" cy="12" r="10" stroke="currentColor" strokeWidth="4"></circle>
                      <path className="opacity-75" fill="currentColor" d="M4 12a8 8 0 018-8V0C5.373 0 0 5.373 0 12h4zm2 5.291A7.962 7.962 0 014 12H0c0 3.042 1.135 5.824 3 7.938l3-2.647z"></path>
                    </svg>
                    Predicting...
                  </>
                ) : (
                  'Predict Category'
                )}
              </button>
            </form>
          </div>

          {/* Prediction Result */}
          {state.result && (
            <div className="bg-white rounded-2xl shadow-xl p-8 animate-fade-in">
              <div className="text-center mb-6">
                <h2 className="text-2xl font-bold text-gray-800 mb-2">Prediction Result</h2>
                <div className="w-16 h-1 bg-blue-600 mx-auto rounded-full"></div>
              </div>

              <div className="space-y-6">
                {/* Original Description */}
                <div className="bg-gray-50 rounded-lg p-4">
                  <h3 className="text-sm font-medium text-gray-500 mb-1">Original Description</h3>
                  <p className="text-lg font-semibold text-gray-800">{state.result.description}</p>
                </div>

                {/* Predicted Category */}
                <div className="bg-blue-50 rounded-lg p-4">
                  <h3 className="text-sm font-medium text-blue-600 mb-1">Predicted Category</h3>
                  <p className="text-2xl font-bold text-blue-800 capitalize">{state.result.predicted_category}</p>
                </div>

                {/* Confidence Score */}
                <div className="bg-gray-50 rounded-lg p-4">
                  <h3 className="text-sm font-medium text-gray-500 mb-1">Confidence Score</h3>
                  <div className="flex items-center justify-between">
                    <div className="flex items-center space-x-3">
                      <div className={`text-3xl font-bold ${getConfidenceColor(state.result.confidence)}`}>
                        {(state.result.confidence * 100).toFixed(1)}%
                      </div>
                      <span className={`px-3 py-1 rounded-full text-sm font-medium border ${getConfidenceBadgeColor(state.result.confidence)}`}>
                        {state.result.confidence >= 0.8 ? 'High' : state.result.confidence >= 0.6 ? 'Medium' : 'Low'} Confidence
                      </span>
                    </div>
                  </div>
                  
                  {/* Confidence Bar */}
                  <div className="mt-3">
                    <div className="w-full bg-gray-200 rounded-full h-2">
                      <div 
                        className={`h-2 rounded-full transition-all duration-500 ${
                          state.result.confidence >= 0.8 ? 'bg-green-500' : 
                          state.result.confidence >= 0.6 ? 'bg-yellow-500' : 'bg-red-500'
                        }`}
                        style={{ width: `${state.result.confidence * 100}%` }}
                      ></div>
                    </div>
                  </div>
                </div>

                {/* Action Buttons */}
                <div className="flex space-x-4 pt-4">
                  <button
                    onClick={() => setState(prev => ({ ...prev, result: null }))}
                    className="flex-1 bg-gray-100 text-gray-700 py-2 px-4 rounded-lg font-medium hover:bg-gray-200 transition-colors duration-200"
                  >
                    Try Another
                  </button>
                  <button
                    onClick={() => {
                      navigator.clipboard.writeText(JSON.stringify(state.result, null, 2));
                      alert('Result copied to clipboard!');
                    }}
                    className="flex-1 bg-blue-100 text-blue-700 py-2 px-4 rounded-lg font-medium hover:bg-blue-200 transition-colors duration-200"
                  >
                    Copy Result
                  </button>
                </div>
              </div>
            </div>
          )}
        </div>

        {/* Footer Info */}
        <div className="text-center mt-12">
          <p className="text-sm text-gray-500">
            Powered by FastAPI & Machine Learning • Model accuracy: ~44%
          </p>
          <p className="text-xs text-gray-400 mt-2">
            API Endpoint: http://localhost:8000/predict-category
          </p>
        </div>
      </div>

      <style jsx>{`
        @keyframes fade-in {
          from {
            opacity: 0;
            transform: translateY(20px);
          }
          to {
            opacity: 1;
            transform: translateY(0);
          }
        }
        
        .animate-fade-in {
          animation: fade-in 0.5s ease-out;
        }
      `}</style>
    </div>
  );
}
