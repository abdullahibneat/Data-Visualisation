import matplotlib.pyplot as plt
from data import summary_data, plot_titles, plot_y_labels

#
# SHOW DATA WITH SORTED VALUES
# (to decide limits for segmenting data)
#

# Use subplot to display 2x3 gird of plots
fig, axes = plt.subplots(nrows=2, ncols=3)

curr_row = 0
curr_col = 0

for i, col in enumerate(summary_data):
    # Retrieve data
    data = summary_data[col]
    
    # Sort in descending order
    data = data.reindex(data.sort_values(ascending=False).index, axis=1)

    # Display data as bar chart
    plot = data.plot.bar(ax=axes[curr_row, curr_col])

    # Set title, y-label
    plot.set_title(plot_titles[i])
    plot.set_ylabel(plot_y_labels[i])

    curr_col = (curr_col + 1) % 3
    if(curr_col == 0):
        curr_row += 1

plt.show()

#
# SEGMENT DATA
#

# The following values were determined from the above plot:
# avg age: HIGH=45+, MEDIUM=28+, LOW=<28
# total visitors: HIGH=150k+, MEDIUM=50k+, LOW=<50k
# max distance: HIGH=50+, MEDIUM=10+, LOW=<10
# avg time: HIGH=120+, MEDIUM=90+, LOW=<90
# pct female: HIGH=56+, MEDIUM=45+, LOW=<45
# avg spend: HIGH=31+, MEDIUM=16+, LOW=<16
categories = ["High", "Medium", "Low"]
high_thershold = [45, 150000, 50, 120, 56, 31]
medium_threshold = [28, 50000, 10, 90, 45, 16]

for i, col in enumerate(summary_data):
    categories_selected = [[] for _ in range(len(categories))]

    # Retrieve data
    data = summary_data[col]
    
    # Sort in descending order
    data = data.reindex(data.sort_values(ascending=False).index, axis=1)

    # Segment venues
    for (name, value) in data.iteritems():
        category = 2
        if value > high_thershold[i]:
            category = 0
        elif value > medium_threshold[i]:
            category = 1
        categories_selected[category].append(name)

    # Show segmented data
    for j, selected in enumerate(categories_selected):
        # Get all values from the selected column
        data_selected = data[data.index.isin(selected)]

        # Display data as bar chart
        plot = data_selected.plot.bar()

        # Set title, y-label
        plot.set_title(categories[j] + " - " + plot_titles[i])
        plot.set_ylabel(plot_y_labels[i])
        plot.set_ylim(bottom=0)

        # Show plots one at a time
        plt.show()