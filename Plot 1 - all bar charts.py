import matplotlib.pyplot as plt
from data import summary_data

plot_titles = ["Average age of visitors", "Total visitors in 2019", "Maximum distance (in miles) visitors are prepared to travel", "Average time spent by visitors", "Percentage of female visitors", "Average spend of visitors"]
plot_y_labels = ["Age", "Number of visitors", "Distance (miles)", "Time (minutes)", "Female visitors (%)", "Spend (£)"]

for i, col in enumerate(summary_data):
    # Retrieve data
    data = summary_data[col]

    # Display data as bar chart
    plot = data.plot.bar()

    # Set title, y-label
    plot.set_title(plot_titles[i])
    plot.set_ylabel(plot_y_labels[i])

    # Show plots one at a time
    plt.show()