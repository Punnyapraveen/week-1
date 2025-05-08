import numpy as np

# Create a numpy array of sales data
sales_data = np.array([100, 200, 300, 400, 500])

# Calculate the mean
mean = np.mean(sales_data)
print("Mean:", mean)

# Calculate the median
median = np.median(sales_data)
print("Median:", median)

# Calculate the standard deviation
std_dev = np.std(sales_data)
print("Standard Deviation:", std_dev)

# Calculate other statistics
min_value = np.min(sales_data)
max_value = np.max(sales_data)
range_value = np.ptp(sales_data)
print("Min Value:", min_value)
print("Max Value:", max_value)
print("Range:", range_value)

