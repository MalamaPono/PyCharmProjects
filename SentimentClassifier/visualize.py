from matplotlib import pyplot as plt
import pandas as pd

df = pd.read_csv('resulting_data.csv')

# y-axis
retweets = df['Number of Retweets'].tolist()

# x-axis
netScore = df['Net Score'].tolist()

plt.tight_layout()

plt.scatter(netScore,retweets)
plt.title("Number of Retweets vs Net Score")
plt.xlabel("Net Score")
plt.ylabel("Number of Retweets")
plt.show()

