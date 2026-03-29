import pandas as pd
import numpy as np


# Load the data
data = {
    'transaction_id': range(1, 21),
    'date': pd.date_range('2024-10-01', periods=20, freq='D'),
    'region': ['North', 'South', 'East', 'West', None, 'North', 'South', None, 'East', 'West',
               'North', 'South', 'East', 'West', 'North', None, 'East', 'West', 'North', 'South'],
    'product_category': ['Electronics', 'Clothing', None, 'Books', 'Electronics', 'Home', 
                         'Clothing', 'Books', 'Electronics', None, 'Home', 'Clothing', 
                         'Books', 'Electronics', 'Home', 'Clothing', 'Books', 'Electronics', 
                         'Home', 'Clothing'],
    'sales_amount': [1200, 450, 890, None, 1500, 670, None, 340, 2100, 780, 
                     560, None, 420, 1800, 920, 510, 380, None, 1100, 640],
    'quantity': [2, 5, 3, 1, None, 4, 2, 3, 1, 5, 
                 3, 2, None, 1, 4, 3, 2, 1, None, 4],
    'customer_age': [25, 34, None, 45, 29, None, 38, 52, 27, 41, 
                     33, None, 48, 26, 35, 42, None, 31, 39, 44],
    'payment_method': ['Credit Card', 'UPI', 'Cash', 'Debit Card', 'Credit Card', 
                       'UPI', 'Cash', None, 'Credit Card', 'UPI', 'Debit Card', 
                       'Cash', 'Credit Card', None, 'UPI', 'Cash', 'Debit Card', 
                       'Credit Card', 'UPI', None]
}

df = pd.DataFrame(data)

# 1. Region & Product_category: Fill with mode
df['region'] = df['region'].fillna(df['region'].mode()[0])
df['product_category'] = df['product_category'].fillna(df['product_category'].mode()[0])

# 2. Sales_amount: Fill with median
df['sales_amount'] = df['sales_amount'].fillna(df['sales_amount'].median())

# 3. Quantity: Fill using forward fill (ffill)
df['quantity'] = df['quantity'].ffill()

# 4. Customer_age: Fill with mean (rounded to integer)
df['customer_age'] = df['customer_age'].fillna(round(df['customer_age'].mean()))

# 5. Payment_method: Drop rows where payment_method is missing
df.dropna(subset=['payment_method'], inplace=True)

# Verify no missing values remain
print("--- Missing Values After Cleaning ---")
print(df.isna().sum())

# Display the first few rows of the cleaned data
print("\n--- Cleaned DataFrame Preview ---")
print(df.head())