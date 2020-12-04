from matplotlib import pyplot as plt
import numpy as np
from data import summary_data

# From previous plot, the following had strong correlation:
# 
# visitor vs distance = 0.94
# age vs spend = 0.68
#
# The first is quite obvious: the more distance people are willing
# to travel, the higher the number of visits.
#
# The second is more interesting, so generate scatter plot for it.
x = summary_data["age"]
y = summary_data["spend"]

# Plot scattergraph
plt.scatter(x, y)

# Find line of best fit (trendline)
z = np.polyfit(x, y, 1)
trend = np.poly1d(z)

# Draw line manually to show dotted line correctly
# Otherwise, doing "plt.plot(x, trend(x), color="r", linestyle="--")"
# shows a series of points regardless of linestyle
trend_x = [min(x), max(x)]
trend_y = [trend(min(x)), trend(max(x))]
plt.plot(trend_x, trend_y, color="r", linestyle="--")

# Set title, axis labels
plt.title("Age vs Spend")
plt.xlabel("Age")
plt.ylabel("Spend (£)")
plt.ylim(bottom=0)

# Show plot
plt.show()