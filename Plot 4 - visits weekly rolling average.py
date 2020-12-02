import matplotlib.pyplot as plt
from data import visitor_data

# Import segmented visitor venues from previous plot
plot3 = __import__("Plot 3 - daily visits time series")
categories = plot3.categories
categories_selected = plot3.categories_selected

# Define rolling average period (in days)
period = 7

for i, selected in enumerate(categories_selected):
    # Get all values from the selected column
    # Use daily visitor data to create time series plot
    data_selected = visitor_data[selected]

    # Calculate rolling average
    averaged_data = data_selected.rolling(window=period).mean()

    # Display original data
    plot = data_selected.plot(linewidth=0.5)

    # Overlay averaged data
    plt.gca().set_prop_cycle(None)
    plt.plot(averaged_data, linewidth=2)

    # Set title, y-label
    plot.set_title(categories[i] + " - visitors over the year 2019 with 7-day rolling average")
    plot.set_ylabel("Visitors")
    plot.set_ylim(bottom=0)

    # Show plots one at a time
    plt.show()