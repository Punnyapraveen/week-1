import pandas as pd

# Create a dummy CSV file
data = {'Product': ['A', 'B', 'C', 'D', 'E'],
        'Sales': [100, 200, 300, 400, 500]}
df = pd.DataFrame(data)
df.to_csv('sales_data.csv', index=False)

# Read the CSV file
df = pd.read_csv('sales_data.csv')

# Print the first few rows of the dataframe
print(df.head())

# Calculate the total sales
total_sales = df['Sales'].sum()
print("Total Sales:", total_sales)

# Calculate the average sales
average_sales = df['Sales'].mean()
print("Average Sales:", average_sales)

# Group the data by product and calculate the total sales for each product
product_sales = df.groupby('Product')['Sales'].sum()
print(product_sales)
# Filter the data for products with sales greater than 300
filtered_data = df[df['Sales'] > 300]
print(filtered_data)

# Sort the data by sales in descending order
sorted_data = df.sort_values(by='Sales', ascending=False)
print(sorted_data)



