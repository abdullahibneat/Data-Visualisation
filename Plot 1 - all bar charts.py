import matplotlib.pyplot as plt
from data import summary_data, plot_titles, plot_y_labels

# Use subplot to display 2x3 gird of plots
fig, axes = plt.subplots(nrows=2, ncols=3)

curr_row = 0
curr_col = 0

for i, col in enumerate(summary_data):
    # Retrieve data
    data = summary_data[col]

    # Display data as bar chart
    plot = data.plot.bar(ax=axes[curr_row, curr_col])

    # Set title, y-label
    plot.set_title(plot_titles[i])
    plot.set_ylabel(plot_y_labels[i])
    plot.set_ylim(bottom=0)

    curr_col = (curr_col + 1) % 3
    if(curr_col == 0):
        curr_row += 1

plt.show()