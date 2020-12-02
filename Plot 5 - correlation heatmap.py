import seaborn as sns
from matplotlib import pyplot as plt
from data import summary_data

corr = summary_data.corr()
ax = sns.heatmap(corr, vmin=-1, vmax=1, center=0, cmap=sns.diverging_palette(220, 20, n=200), square=True, annot=True)
plt.title("Correlation heatmap")
plt.show()