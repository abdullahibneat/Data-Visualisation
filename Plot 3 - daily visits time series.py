import matplotlib.pyplot as plt
from data import summary_data, visitor_data

# The following thresholds were determined from the previous plot:
#
# total visitors: HIGH=150k+, MEDIUM=50k+, LOW=<50k
#
# Because the "low" graph produces too many lines,
# added a very low threshold for visitors less than 18k
categories = ["High", "Medium", "Low", "Very Low"]
high_thershold = 150000
medium_threshold = 50000
low_threshold = 18000

# Retrieve data
# To segment daily visitor data, use summary_data to compare
# total number of visitors for each venue
data = summary_data["visitors"]

# Segment venues
categories_selected = [[] for _ in range(len(categories))]

for (name, value) in data.iteritems():
    category = 3
    if value > high_thershold:
        category = 0
    elif value > medium_threshold:
        category = 1
    elif value > low_threshold:
        category = 2
    categories_selected[category].append(name)

if __name__ == "__main__":
    # Use subplot to display 2x2 gird of plots
    fig, axes = plt.subplots(nrows=2, ncols=2)

    curr_row = 0
    curr_col = 0
    
    # Show segmented data
    for i, selected in enumerate(categories_selected):
        # Get all values from the selected column
        # Use daily visitor data to create time series plot
        data_selected = visitor_data[selected]

        # Display data as bar chart
        plot = data_selected.plot(ax=axes[curr_row, curr_col])

        # Set title, y-label
        plot.set_title(categories[i] + " - visitors over the year 2019")
        plot.set_ylabel("Visitors")
        plot.set_ylim(bottom=0)

        curr_col = (curr_col + 1) % 2
        if(curr_col == 0):
            curr_row += 1

plt.show()