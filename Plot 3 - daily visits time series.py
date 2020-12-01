import matplotlib.pyplot as plt
from data import summary_data, visitor_data

# From previous plot:
# total visitors: HIGH=150k+, MEDIUM=50k+, LOW=<50k
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

# Show segmented data
for i, selected in enumerate(categories_selected):
    # Get all values from the selected column
    # Use daily visitor data to create time series plot
    data_selected = visitor_data[selected]

    # Display data as bar chart
    plot = data_selected.plot()

    # Set title, y-label
    plot.set_title(categories[i] + " - visitors over the year 2019")
    plot.set_ylabel("Visitors")

    # Show plots one at a time
    plt.show()