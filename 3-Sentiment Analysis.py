# start by reading in the corpus, which preserves word order
import pandas as pd

data = pd.read_pickle('data_clean_m.pkl')

# Create quick lambda functions to find the polarity and subjectivity of each movie script
from textblob import TextBlob

pol = lambda x: TextBlob(x).sentiment.polarity
sub = lambda x: TextBlob(x).sentiment.subjectivity

data['polarity'] = data['script'].apply(pol)
data['subjectivity'] = data['script'].apply(sub)
#print(data)

# plot the results
import matplotlib.pyplot as plt

plt.rcParams['figure.figsize'] = [10, 8]

for index, movies in enumerate(data.index):
    x = data.polarity.loc[movies]
    y = data.subjectivity.loc[movies]
    plt.scatter(x, y, color='blue')
    plt.text(x+.001, y+.001, movies, fontsize=10)
    plt.xlim(-.01, .12) 
    
plt.title('Sentiment Analysis', fontsize=20)
plt.xlabel('<-- Negative -------- Positive -->', fontsize=15)
plt.ylabel('<-- Facts -------- Opinions -->', fontsize=15)

plt.show()