import matplotlib.pyplot as plt
import pandas as pd

# Read the CSV file
df = pd.read_csv('sales_data.csv')

# Plot a bar chart of sales by product
plt.bar(df['Product'], df['Sales'])
plt.xlabel('Product')
plt.ylabel('Sales')
plt.title('Sales by Product')
plt.xticks(rotation=45)
plt.show()

# Customize the plot
plt.figure(figsize=(10,6))
plt.bar(df['Product'], df['Sales'], color='skyblue')
plt.xlabel('Product', fontsize=14)
plt.ylabel('Sales', fontsize=14)
plt.title('Sales by Product', fontsize=16)
plt.xticks(rotation=45)
plt.tight_layout()
plt.show()

