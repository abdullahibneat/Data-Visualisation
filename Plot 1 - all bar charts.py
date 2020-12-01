import matplotlib.pyplot as plt
from data import summary_data, plot_titles, plot_y_labels

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