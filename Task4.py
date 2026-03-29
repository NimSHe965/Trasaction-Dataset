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


# 1. Create a function sales_range() that returns max - min
def sales_range(series):
    return series.max() - series.min()

# 2. Apply it to find sales range for each region
# We use .agg() with our custom function name
region_range = df.groupby('region')['sales_amount'].agg(sales_range)

print("--- Sales Range (Max - Min) by Region ---")
print(region_range)
print("\n")

# 3. Use .agg() to calculate multiple metrics by region:
# sales_amount: sum, mean, max
# quantity: sum, min
region_summary = df.groupby('region').agg({
    'sales_amount': ['sum', 'mean', 'max'],
    'quantity': ['sum', 'min']
})

print("--- Multi-Metric Summary by Region ---")
print(region_summary)