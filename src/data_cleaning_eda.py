import os
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns

def run_eda():
    data_path = os.path.join("data", "sales_data.csv")
    if not os.path.exists(data_path):
        data_path = "sales_data.csv"
        
    print(f"[1/4] Loading dataset from: {data_path}")
    df = pd.read_csv(data_path)
    
    print("\n--- Dataset Info & Summary ---")
    print(df.info())
    print("\n--- Descriptive Statistics ---")
    print(df.describe().T)
    
    # Check Missing Values
    print("\n--- Missing Values Count ---")
    print(df.isnull().sum())
    
    # Feature Engineering
    df['Date'] = pd.to_datetime(df['Date'])
    df['Profit_Margin_%'] = (df['Profit'] / df['Sales']) * 100
    
    # Output Directory for Charts
    os.makedirs("reports", exist_ok=True)
    
    # Chart 1: Total Sales by Category
    plt.figure(figsize=(8, 4.5))
    cat_sales = df.groupby('Category')['Sales'].sum().reset_index()
    sns.barplot(data=cat_sales, x='Category', y='Sales', palette='Blues_r')
    plt.title('Total Revenue by Product Category (2024)')
    plt.ylabel('Sales ($)')
    plt.tight_layout()
    plt.savefig(os.path.join("reports", "category_sales_chart.png"))
    plt.close()
    
    # Chart 2: Correlation Heatmap
    plt.figure(figsize=(7, 5))
    num_cols = df.select_dtypes(include=[np.number]).columns
    sns.heatmap(df[num_cols].corr(), annot=True, cmap='Blues', fmt='.2f')
    plt.title('Correlation Matrix (Sales, Marketing Spend, Units, Profit)')
    plt.tight_layout()
    plt.savefig(os.path.join("reports", "correlation_heatmap.png"))
    plt.close()
    
    print("\n[SUCCESS] EDA complete! Visual charts saved to 'reports/' directory.")

if __name__ == "__main__":
    run_eda()