# Visualization coursework

The `data.py` file contains the data from the `/data/*.csv` files within a `summary_data` dataframe. Run each python file to see individual visualizations.

## Scenario

ChrisCo is a fictional, but nonetheless very successful, company managing a range of venues across the UK. ChrisCo collects a huge amount of data about individual customers visiting its venues using its loyalty card scheme but this customer data has been aggregated/averaged to give information about the company’s 40 venues, each identified by a unique 3 letter code (e.g. ABC, XYZ, etc).

You should compile the data into two dataframes: one containing daily visitor data (one row for each date); the other containing summary data (one row for each venue), compiled from all of the .csv files, including the daily visitors. Your task is to explore this data visually and present conclusions about any characteristics you discover (e.g. correlations), together with a suggestion about how the data might be segmented.

## Visualization 1 – all data as bar chart
<p align="center">
    <img alt="Figure 1: Overview of dataset" src="https://i.imgur.com/nj2yQ8O.png">
    <p align="center"><b>Figure 1: </b><i>Overview of dataset</i></p>
</p>

**Justification:** This visualization was produced to get a sense of the data that was given to me. This shows the entirety of the data as bar charts as opposed to reading through each line of the csv files manually.

**Explanation:** The bar charts in figure 1 show that the data is about 40 venues, and contains the following information (from left to right, top to bottom):

-	Average age of visitors
-	Total number of visitors
-	Maximum distance (in miles) visitors are prepared to travel
-	Average time spent by visitors
-	Percentage of female visitors
-	Average spend of visitors

These charts however are slightly difficult to read, especially when trying to identify the venues that perform better than others. The next visualization will sort this data to solve this issue.

## Visualization 2 – sorted data
<p align="center">
    <img alt="Figure 2: Data sorted in descending order" src="https://imgur.com/9a6TeT7.png">
    <p align="center"><b>Figure 2: </b><i>Data sorted in descending order</i></p>
</p>

**Justification:** In the previous visualization (figure 1), it is quite challenging to identify which venues perform better than others. To improve readability, the data has been sorted in descending order.

**Explanation:** In figure 2 we can identify which venues are the best and worst performers for each category. Furthermore, it allows us to segment the data into 3 categories: high performers, medium performers and low performers. The thresholds have been identified as follows:

|                     | High  | Medium     | Low   |
| ------------------- | ----- | ---------- | ----- |
| Average age         | 45+   | 28 - 45    | < 28  |
| Total visitors      | 125k+ | 50k - 125k | < 50k |
| Travelling distance | 40+   | 20 - 40    | < 10  |
| Time spent          | 120+  | 90 - 120   | < 90  |
| Female percentage   | 56+   | 45 - 56    | <45   |
| Average spend       | 31+   | 16 - 31    | <16   |

Based on these boundaries, we can observe that although venues with a low number of visitors individually contribute very little to the overall number of visitors, combining them show how they produce a significant influx of visitors (more specifically 632,082 people: over 3x more than the most visited venue, while looking at venues with less than 18k visitors amounts to 86,783 visitors, equivalent to a medium performing venue).

## Visualization 3 – daily visits
<p align="center">
    <img alt="Figure 3: Daily visits over the year 2019" src="https://imgur.com/pduA44J.png">
    <p align="center"><b>Figure 3: </b><i>Daily visits over the year 2019</i></p>
</p>

**Justification:** Since the data related to daily number of visits contains information for every day of the year 2019, it can be useful to see this data as a time series to get an idea of how many visitors have been recorded over the year.

**Explanation:** In the previous visualization (figure 2) I identified some thresholds to segment each category. The segmentation has been applied to the “daily visits” plot to show the flow of visitors over the year. A further category of “very low” (less than 18k visitors) has been added to clean up the graph and improve readability.

Although the high, medium and low categories have regular peaks and troughs, the plots show quite a steady and linear number of visitors, with no sign of increase or decline over the year. However, the same cannot be said about venues with a very low number of visitors, where some venues appear to have no visitors at all during some parts of the year. This has been the subject of analysis for the next visualization.

## Visualization 4 – weekly visits (rolling average)
<p align="center">
    <img alt="Figure 4: Daily visits of very low performing venues over the year 2019" src="https://imgur.com/xHmm0jZ.png">
    <p align="center"><b>Figure 4: </b><i>Daily visits of very low performing venues over the year 2019</i></p>
</p>

**Justification:** In the previous visualization (figure 3) high, medium and low visitors had a steady average over the year, but the very low visitors was quite different, with some venues having no visitors at all at some points. To present this data more clearly, a weekly rolling average has been applied to remove some of the noise to improve readability without completely obscuring the noise.

**Explanation:** In figure 4 the daily number of visits is displayed for visits with a very low turnout. A weekly rolling average has been added as an overlay to better visualize the data and remove some of the noise. For each day, an average of the last 7 days is calculated to plot the next point. Due to this, the first 7 days of the year are not computed, since it would require information from the previous year.

This graph clearly shows that venues ZPL and XXO had a steady number of visits until July 2019, after which it drops to 0; ZJB and BQV had no visitors before April 2019; YDI and BKI had no visitors before July 2019; YVW and AEQ had no visitors before October 2019.

This could be because of missing data, which has been replaced with the value 0, or could indicate that ZPL and XXO were shut down around July 2019, with the rest being opened throughout 2019. The latter venues also show an increase in the number of visitors, strongly indicating that these venues have probably been newly opened. Missing values on the other hand would have displayed the data more similar to figure 3, with a linear steady number of visits.

## Visualization 5 – correlation
<p align="center">
    <img alt="Figure 5: Correlation against 2 variables" src="https://imgur.com/WLDEr0P.png">
    <p align="center"><b>Figure 5: </b><i>Correlation against 2 variables</i></p>
</p>

**Justification:** It can be useful to see if there are any correlations between any 2 variables in the dataset to gather insight on which 2 variables affect each other. Using a heatmap, the correlation can be visualized by computing the correlation coefficient. This is opposed to manually picking two variables and find the correlation by hand, producing quite a large number of graphs (15 to be more precise). From a heatmap, it’s easy to see at a glance which variables have a strong positive correlation (values close to +1) and which have a strong negative correlation (values close to -1).

**Explanation:** In the heatmap shown in figure 5, we can see which pairs of variables (age, visitors, distance, duration, female and spend) are strongly dependent on each other (positive/negative correlation, values closer to 1 and -1), and which pairs aren’t (no correlation, values closer to 0). Values along the diagonal can be ignored, since a variable is strongly correlated with themselves.

We can see that 2 values stand out from the rest:

-	Visitors vs Distance (0.94): this is quite obvious, since visitors willing to travel longer distances will probably visit other venues, thus increase the overall number of visits of the company.

-	Age vs Spend (0.68): this is interesting, since it indicates that older visitors are the ones spending more for each visit compared to younger visitors. Although the correlation is not very strong as the previous one, it is quite significant. This will be analysed in the next visualization.

No significantly strong negative correlations have been identified.

## Visualization 6 – Age vs Spend
<p align="center">
    <img alt="Figure 6: Correlation against age and spend" src="https://imgur.com/YOr46Xj.png">
    <p align="center"><b>Figure 6: </b><i>Correlation between age and spend</i></p>
</p>

**Justification:** in the previous visualization (figure 5), “age vs spend” had the second highest correlation coefficient. This was identified as an interesting comparison, and a plot was generated in figure 6 to demonstrate the numbers compared against each other. Additionally, trendline was added to show the overall direction of the correlation.

**Explanation:** To demonstrate how closely related “age” and “spend” are, I plotted an “age vs spend” scatterplot (figure 6) to see the spread of the values. A tight spread will indicate a very strong relationship between the two. We already know from figure 5 that the spread will be quite high, since the correlation coefficient is not very close to +1. Additionally, a line of best fit (in red) has been overlayed to show the general direction of the correlation.

It is clear that the older a visitor is, the more they are willing to spend at the venue. It shows that the oldest spend as much as twice as the youngest visitors, indicating an area of improvement to increase younger visitors’ engagement to boost sales. However, more data is required to validate this theory. This could be in the form of daily transaction records alongside the age of visitors.
