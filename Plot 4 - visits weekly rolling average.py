import matplotlib.pyplot as plt
from data import visitor_data

# Import segmented visitor venues from previous plot
plot3 = __import__("Plot 3 - daily visits time series")
very_low_venues = plot3.categories_selected[-1]

# Define rolling average period (in days)
period = 7

data_selected = visitor_data[very_low_venues]

# Calculate rolling average
averaged_data = data_selected.rolling(window=period).mean()

# Display original data
plt.plot(data_selected, linewidth=0.5)

# Overlay averaged data
plt.gca().set_prop_cycle(None)
plt.plot(averaged_data, linewidth=2)

# Set title, y-label, show figure
plt.title("Very low - visitors over the year 2019 with 7-day rolling average")
plt.ylabel("Visitors")
plt.ylim(bottom=0)
plt.legend(data_selected)

plt.show()