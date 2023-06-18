import pandas as pd
import random
from datetime import datetime, timedelta

# Define the number of rows and columns
num_rows = 10000
num_cols = 19

# Generate the random dataset
data = []
start_date = datetime(2023, 1, 1)
end_date = start_date + timedelta(days=364)  # Assuming a 365-day financial year
date_range = pd.date_range(start=start_date, end=end_date).tolist()  # Convert date_range to a list

for _ in range(num_rows):
    transaction_id = random.randint(100000, 999999)
    date = random.choice(date_range)  # Select a random date from the date_range list
    product_category = random.choice(['Electronics', 'Fashion', 'Home & Kitchen', 'Beauty'])
    
    if product_category == 'Electronics':
        product_subcategory = random.choice(['Mobiles', 'Laptops', 'TVs', 'Audio Player'])
    elif product_category == 'Fashion':
        product_subcategory = random.choice(['Clothing', 'Shoes', 'Accessories'])
    elif product_category == 'Home & Kitchen':
        product_subcategory = random.choice(['Appliances', 'Furniture', 'Decor', 'Cookware'])
    else:
        product_subcategory = random.choice(['Skincare', 'Makeup', 'Haircare', 'Fragrances'])
    
    quantity = random.randint(1, 5)
    price_per_unit = round(random.uniform(5000, 50000), 2)
    total_sales = round(quantity * price_per_unit, 2)
    cost_of_goods_sold = round(total_sales * random.uniform(0.6, 0.8), 2)
    marketing_expense = round(total_sales * random.uniform(0.05, 0.1), 2)
    shipping_expense = round(quantity * random.uniform(50, 500), 2)
    discount_applied = random.choice(['5%', '10%', '15%', 'No Discount'])
    customer_id = random.randint(1001, 9999)
    region = random.choice(['Punjab', 'Himachal Pradesh', 'Haryana', 'Uttarakhand', 'Madhya Pradesh', 'Maharastra','Gujrat'])  # Modify regions as per your requirement
    profit = round(total_sales - cost_of_goods_sold - marketing_expense - shipping_expense, 2)
    tax = round(total_sales * random.uniform(0.05, 0.15), 2)
    payment_method = random.choice(['Credit Card', 'Debit Card', 'Cash', 'UPI'])
    day_of_week = date.strftime('%A')
    month = date.strftime('%B')
    quarter = 'Q' + str((date.month - 1) // 3 + 1)
    customer_segment = random.choice(['High-Value', 'Mid-Value', 'Low-Value'])
    sales_channel = random.choice(['Online', 'Offline', 'Retail Store'])
    product_rating = round(random.uniform(1.0, 5.0), 2)

    data.append([
        transaction_id, date, product_category, product_subcategory, quantity, price_per_unit, total_sales,
        cost_of_goods_sold, marketing_expense, shipping_expense, discount_applied,
        customer_id, region, profit, tax, payment_method, day_of_week, month, quarter, customer_segment,
        sales_channel, product_rating
    ])

# Create a pandas DataFrame from the generated data
columns = [
    'Transaction ID', 'Date', 'Product Category', 'Product Subcategory', 'Quantity', 'Price per Unit', 'Total Sales',
    'Cost of Goods Sold', 'Marketing Expense', 'Shipping Expense', 'Discount Applied',
    'Customer ID', 'Region', 'Profit', 'Tax', 'Payment Method', 'Day of Week', 'Month', 'Quarter',
    'Customer Segment', 'Sales Channel', 'Product Rating'
]
df = pd.DataFrame(data, columns=columns)

# Save the DataFrame to a CSV file
df.to_csv('sales_dataset.csv', index=False)
