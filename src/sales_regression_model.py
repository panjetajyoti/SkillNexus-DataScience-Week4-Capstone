import os
import pandas as pd
import numpy as np
from sklearn.model_selection import train_test_split
from sklearn.linear_model import LinearRegression
from sklearn.metrics import mean_squared_error, r2_score
import matplotlib.pyplot as plt

def build_regression_model():
    data_path = os.path.join("data", "sales_data.csv")
    if not os.path.exists(data_path):
        data_path = "sales_data.csv"
        
    df = pd.read_csv(data_path)
    
    # Features & Target Variable
    # Target: Sales
    # Predictors: Units_Sold, Unit_Price, Marketing_Spend, Discount
    feature_cols = ['Units_Sold', 'Unit_Price', 'Marketing_Spend', 'Discount']
    X = df[feature_cols]
    y = df['Sales']
    
    # Train-Test Split (80% Train, 20% Test)
    X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)
    
    # Initialize & Fit Model
    model = LinearRegression()
    model.fit(X_train, y_train)
    
    # Predictions
    y_pred = model.predict(X_test)
    
    # Metrics
    r2 = r2_score(y_test, y_pred)
    rmse = np.sqrt(mean_squared_error(y_test, y_pred))
    
    print("\n==========================================")
    print("      SALES REGRESSION MODEL RESULTS       ")
    print("==========================================")
    print(f"R-squared Score (R²): {r2:.4f} (Model explains {r2*100:.1f}% variance)")
    print(f"Root Mean Squared Error (RMSE): ${rmse:.2f}")
    print("\n--- Feature Coefficients ---")
    for col, coef in zip(feature_cols, model.coef_):
        print(f"  • {col:18}: {coef:10.4f}")
    print(f"  • Intercept         : {model.intercept_:10.4f}")
    print("==========================================\n")
    
    # Save Prediction Chart
    os.makedirs("reports", exist_ok=True)
    plt.figure(figsize=(6.5, 4.5))
    plt.scatter(y_test, y_pred, color='#1F4E79', s=80, edgecolors='black')
    plt.plot([y.min(), y.max()], [y.min(), y.max()], 'r--', lw=2, label='Perfect Fit')
    plt.xlabel('Actual Sales ($)')
    plt.ylabel('Predicted Sales ($)')
    plt.title(f'Actual vs Predicted Sales (R² = {r2:.2f})')
    plt.legend()
    plt.grid(True, linestyle='--', alpha=0.5)
    plt.tight_layout()
    plt.savefig(os.path.join("reports", "regression_actual_vs_predicted.png"))
    plt.close()
    print("[SUCCESS] Regression model fitted and chart saved to 'reports/'!")

if __name__ == "__main__":
    build_regression_model()