import pandas as pd

# Average age of visitors
age_data = pd.read_csv("data/VenueAge.csv", index_col=0)  # index_col=0 tells pandas to use first column as index

# Daily number of visitors
visitor_data = pd.read_csv("data/VenueDailyVisitors.csv", index_col=0)
visitor_data.index = pd.to_datetime(visitor_data.index)  # Visitor data uses dates, convert dates to datetime

# Maximum distance (in miles) visitors are prepared to travel
distance_data = pd.read_csv("data/VenueDistance.csv", index_col=0)

# Average time spent by visitors
duration_data = pd.read_csv("data/VenueDuration.csv", index_col=0)

# Percentage of female visitors
gender_data = pd.read_csv("data/VenueGender.csv", index_col=0)

# Average spend of each visitor
spend_data = pd.read_csv("data/VenueSpend.csv", index_col=0)

# Compile data into a dataframe
summary_data = pd.DataFrame(index=visitor_data.columns)
summary_data["age"] = age_data.values
summary_data["visitors"] = visitor_data.sum().values
summary_data["distance"] = distance_data.values
summary_data["duration"] = duration_data.values
summary_data["female"] = gender_data.values
summary_data["spend"] = spend_data.values

print(summary_data.head())