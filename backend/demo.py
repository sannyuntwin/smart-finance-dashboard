"""
Demo script showing how to use the Smart Finance Dashboard API
"""

import requests
import json

def demo_api():
    """Demonstrate API usage with examples"""
    base_url = "http://localhost:8000"
    
    print("🚀 Smart Finance Dashboard API Demo")
    print("=" * 50)
    
    # Example transactions to categorize
    transactions = [
        "Grab Food",
        "Netflix Subscription", 
        "Shopee Shopping",
        "Uber Ride",
        "Monthly Salary",
        "McDonald's Dinner",
        "Spotify Premium",
        "Amazon Purchase",
        "Gas Station",
        "Freelance Payment"
    ]
    
    print(f"\n📊 Testing {len(transactions)} transactions:")
    print("-" * 50)
    
    correct_predictions = 0
    
    for i, description in enumerate(transactions, 1):
        try:
            # Make API request
            response = requests.post(
                f"{base_url}/predict-category",
                json={"description": description},
                headers={"Content-Type": "application/json"}
            )
            
            if response.status_code == 200:
                result = response.json()
                predicted = result['predicted_category']
                confidence = result['confidence']
                
                # Simple validation (you could make this more sophisticated)
                expected = get_expected_category(description)
                is_correct = predicted.lower() == expected.lower()
                if is_correct:
                    correct_predictions += 1
                
                status = "✅" if is_correct else "❌"
                print(f"{i:2d}. {description:<25} → {predicted:<12} ({confidence:.2%}) {status}")
                
            else:
                print(f"{i:2d}. {description:<25} → ERROR: {response.status_code}")
                
        except Exception as e:
            print(f"{i:2d}. {description:<25} → ERROR: {e}")
    
    # Summary
    accuracy = (correct_predictions / len(transactions)) * 100
    print("-" * 50)
    print(f"📈 Results: {correct_predictions}/{len(transactions)} correct ({accuracy:.1f}% accuracy)")
    
    print(f"\n🌐 API Documentation:")
    print(f"   Swagger UI: {base_url}/docs")
    print(f"   ReDoc: {base_url}/redoc")
    print(f"   Health Check: {base_url}/health")

def get_expected_category(description):
    """Simple function to get expected category for demo purposes"""
    description_lower = description.lower()
    
    if any(food in description_lower for food in ['food', 'mcdonald', 'dinner']):
        return 'Food'
    elif any(ent in description_lower for ent in ['netflix', 'spotify']):
        return 'Entertainment'
    elif any(shop in description_lower for shop in ['shopee', 'amazon', 'shopping']):
        return 'Shopping'
    elif any(trans in description_lower for trans in ['uber', 'gas', 'ride']):
        return 'Transport'
    elif any(inc in description_lower for inc in ['salary', 'freelance', 'payment']):
        return 'Income'
    else:
        return 'Unknown'

if __name__ == "__main__":
    demo_api()
