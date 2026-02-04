import requests

# This simulates a transaction with 5 features
transaction_data = {"features": [450, 1.5, 0.2, 5, 80]}

# Sending the data to your API
response = requests.post('http://127.0.0.1:5001/check_transaction', json=transaction_data)

print("API Response:", response.json())