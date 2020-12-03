from matplotlib import pyplot as plt
from data import summary_data

# From previous plot, the following had strong correlation:
# 
# visitor vs distance = 0.94
# age vs spend = 0.68
#
# The first is quite obvious: the more distance people are willing
# to travel, the higher the number of visits.
#
# The second is more interesting, so generate scatter plot for it.
plt.scatter(summary_data["age"], summary_data["spend"])
plt.title("Age vs Spend")
plt.xlabel("Age")
plt.ylabel("Spend (£)")
plt.show()