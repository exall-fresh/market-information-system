import matplotlib.pyplot as plt
import numpy as np

# Example data
markets = ['Market A', 'Market B', 'Market C', 'Market D', 'Market E', 'Market F', 'Market G']
products = ['Mangoes', 'Maize', 'Chicken']

# Prices for each product in each market
mango_prices = [10, 15, 20, 25, 13, 18, 22]
maize_prices = [8, 12, 16, 20, 14, 18, 24]
chicken_prices = [18, 25, 30, 35, 22, 28, 32]

# Combining prices for all products
all_prices = [mango_prices, maize_prices, chicken_prices]

# Calculate average prices for each market for all products
average_prices = [np.mean(prices) for prices in zip(*all_prices)]

# Plotting the bar chart
plt.figure(figsize=(10, 6))
barWidth = 0.25

r1 = np.arange(len(markets))
r2 = [x + barWidth for x in r1]
r3 = [x + barWidth for x in r2]

plt.bar(r1, mango_prices, color='skyblue', width=barWidth, label='Mangoes')
plt.bar(r2, maize_prices, color='orange', width=barWidth, label='Maize')
plt.bar(r3, chicken_prices, color='green', width=barWidth, label='Chicken')

plt.xlabel('Markets')
plt.ylabel('Prices')
plt.title('Prices of Products Across Markets')
plt.xticks([r + barWidth for r in range(len(markets))], markets)
plt.legend()
plt.tight_layout()

# Show the plot
plt.show()
