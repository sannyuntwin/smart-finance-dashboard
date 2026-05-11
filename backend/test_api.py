"""
Test script for the Smart Finance Dashboard API
"""

import requests
import json

def test_api():
    """Test the API endpoints"""
    base_url = "http://localhost:8000"
    
    print("Testing Smart Finance Dashboard API")
    print("=" * 50)
    
    # Test 1: Health check
    print("\n1. Testing health endpoint...")
    try:
        response = requests.get(f"{base_url}/health")
        print(f"Status: {response.status_code}")
        print(f"Response: {response.json()}")
    except Exception as e:
        print(f"Error: {e}")
        return
    
    # Test 2: Root endpoint
    print("\n2. Testing root endpoint...")
    try:
        response = requests.get(f"{base_url}/")
        print(f"Status: {response.status_code}")
        print(f"Response: {response.json()}")
    except Exception as e:
        print(f"Error: {e}")
    
    # Test 3: Categories endpoint
    print("\n3. Testing categories endpoint...")
    try:
        response = requests.get(f"{base_url}/categories")
        print(f"Status: {response.status_code}")
        print(f"Response: {response.json()}")
    except Exception as e:
        print(f"Error: {e}")
    
    # Test 4: Prediction endpoint with sample data
    print("\n4. Testing prediction endpoint...")
    test_cases = [
        "Grab Food",
        "Netflix",
        "Shopee",
        "Grab Car",
        "Salary",
        "McDonald's",
        "Spotify",
        "Amazon"
    ]
    
    for description in test_cases:
        try:
            print(f"\nTesting: '{description}'")
            payload = {"description": description}
            response = requests.post(
                f"{base_url}/predict-category",
                json=payload,
                headers={"Content-Type": "application/json"}
            )
            print(f"Status: {response.status_code}")
            print(f"Response: {response.json()}")
        except Exception as e:
            print(f"Error: {e}")
    
    # Test 5: Error handling - empty description
    print("\n5. Testing error handling with empty description...")
    try:
        payload = {"description": ""}
        response = requests.post(
            f"{base_url}/predict-category",
            json=payload,
            headers={"Content-Type": "application/json"}
        )
        print(f"Status: {response.status_code}")
        print(f"Response: {response.json()}")
    except Exception as e:
        print(f"Error: {e}")

if __name__ == "__main__":
    test_api()
