import random
from faker import Faker
import pandas as pd
from datetime import datetime, timedelta

# Initialize Faker and random seed
fake = Faker()
random.seed(42)

# Define possible values for columns
payment_methods = ['Credit Card', 'PayPal', 'Debit Card', 'Bank Transfer', 'Cash']
sale_statuses = ['Completed', 'Pending', 'Canceled']
regions = ['North America', 'Europe', 'Asia', 'Africa', 'South America']
store_ids = [1, 2, 3, 4, 5]  # Example for 5 stores


# Function to generate random sale data
def generate_random_sale_data(num_rows):
    data = []

    for _ in range(num_rows):
        sale_id = fake.unique.random_number(digits=6)
        product_id = random.randint(100, 999)  # Random Product ID
        customer_id = random.randint(2000, 3000)  # Random Customer ID
        sale_amount = round(random.uniform(50.00, 500.00), 2)  # Random sale amount between $50 and $500
        quantity = random.randint(1, 5)  # Random quantity between 1 and 5
        sale_time = fake.date_this_year() + timedelta(hours=random.randint(0, 23), minutes=random.randint(0, 59))
        payment_method = random.choice(payment_methods)
        sale_status = random.choice(sale_statuses)
        discount_applied = random.uniform(0, 20)  # Random discount between 0% and 20%
        total_amount_before_discount = sale_amount / (1 - (discount_applied / 100)) if discount_applied else sale_amount
        region = random.choice(regions)
        store_id = random.choice(store_ids)

        # Append the generated data for this row
        data.append([
            sale_id, product_id, customer_id, sale_amount, quantity, sale_time,
            payment_method, sale_status, round(discount_applied, 2), round(total_amount_before_discount, 2),
            region, store_id
        ])

    return data


# Generate at least 1000 rows of random data
num_rows = 1000
random_sales_data = generate_random_sale_data(num_rows)

# Create a DataFrame from the generated data
columns = [
    'SaleID', 'ProductID', 'CustomerID', 'SaleAmount', 'Quantity', 'SaleTime',
    'PaymentMethod', 'SaleStatus', 'DiscountApplied', 'TotalAmountBeforeDiscount',
    'Region', 'StoreID'
]

df = pd.DataFrame(random_sales_data, columns=columns)

# Save to a CSV file
df.to_csv('random_sales_data.csv', index=False)

# Show the first few rows of the generated data
print(df.head())
