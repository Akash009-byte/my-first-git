import pandas as pd
import numpy as np
from sklearn.ensemble import RandomForestClassifier
from sklearn.model_selection import train_test_split
import joblib


# 1. Generate Synthetic Data
def generate_data():
    np.random.seed(42)
    # Creating 1000 normal transactions and 50 fraudulent ones
    legit = np.random.normal(loc=50, scale=10, size=(1000, 5))
    fraud = np.random.normal(loc=500, scale=50, size=(50, 5))

    X = np.vstack([legit, fraud])
    y = np.array([0] * 1000 + [1] * 50)  # 0 = Legit, 1 = Fraud
    return X, y


# 2. Train the Model
X, y = generate_data()
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2)

model = RandomForestClassifier(n_estimators=100)
model.fit(X_train, y_train)

# 3. Save the model to a file
joblib.dump(model, 'fraud_model.pkl')
print("Success: Model trained and saved as 'fraud_model.pkl'")