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


# 1. Calculate total sales by region
total_sales_by_region = df.groupby('region')['sales_amount'].sum()
print("--- Total Sales by Region ---")
print(total_sales_by_region)
print("\n")

# 2. Calculate average sales by product_category
avg_sales_by_category = df.groupby('product_category')['sales_amount'].mean()
print("--- Average Sales by Product Category ---")
print(avg_sales_by_category)
print("\n")

# 3. Group by both region and product_category, 
# calculate total sales and quantity, then flatten using reset_index()
grouped_data = df.groupby(['region', 'product_category']).agg({
    'sales_amount': 'sum',
    'quantity': 'sum'
}).reset_index()

print("--- Grouped Data (Region & Category) ---")
print(grouped_data)
print("\n")

# 4. Display top 3 region-product combinations by sales
top_3_combos = grouped_data.sort_values(by='sales_amount', ascending=False).head(3)

print("--- Top 3 Region-Product Combinations by Sales ---")
print(top_3_combos)