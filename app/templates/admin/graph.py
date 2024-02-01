import matplotlib.pyplot as plt

# Example data
markets = ['Market A', 'Market B', 'Market C', 'Market D', 'Market E', 'Market F', 'Market G']
products_prices = [
    [10, 15, 20, 25],  # Market A prices for different products
    [12, 18, 22, 28],  # Market B prices for different products
    [9, 14, 19, 24],   # Market C prices for different products
    [11, 16, 21, 26],  # Market D prices for different products
    [13, 17, 23, 27],  # Market E prices for different products
    [8, 12, 18, 21],   # Market F prices for different products
    [10, 13, 20, 25]   # Market G prices for different products
]

# Calculate average prices for each market
average_prices = [sum(prices) / len(prices) for prices in products_prices]

# Plotting the bar chart
plt.figure(figsize=(10, 6))
plt.bar(markets, average_prices, color='skyblue')
plt.xlabel('Markets')
plt.ylabel('Average Prices')
plt.title('Average Prices of Products Across Markets')
plt.xticks(rotation=45)  # Rotate x-axis labels for better readability
plt.tight_layout()

# Show the plot
plt.show()
