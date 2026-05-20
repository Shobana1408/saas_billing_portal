import pandas as pd
from sklearn.linear_model import LinearRegression
import joblib
import numpy as np


def train_revenue_model():

    # Load revenue dataset
    data = pd.read_csv("ai_models/dataset/revenue_data.csv")

    # Prepare features
    X = np.array(range(len(data))).reshape(-1, 1)
    y = data["revenue"]

    # Train model
    model = LinearRegression()
    model.fit(X, y)

    # Save model
    joblib.dump(model, "ai_models/revenue_model.pkl")

    print("Revenue Forecast Model Trained Successfully")


if __name__ == "__main__":
    train_revenue_model()