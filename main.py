import nltk
import random    
import re
import string
import numpy as np
import matplotlib.pyplot as plt
from nltk.corpus import twitter_samples, stopwords
from nltk.tokenize import TweetTokenizer

nltk.download('stopwords')
nltk.download('punkt')
nltk.download('twitter_samples')

all_pos = twitter_samples.strings('positive_tweets.json')
all_neg = twitter_samples.strings('negative_tweets.json')

tweets = all_pos + all_neg
labels = np.append(np.ones((len(all_pos), 1)), np.zeros((len(all_neg), 1)), axis=0)

train_pos, train_neg = all_pos[:4000], all_neg[:4000]
train_x = train_pos + train_neg
print("Number of tweets:", len(train_x))

plt.figure(figsize=(5, 5))
plt.pie(
    [len(all_pos), len(all_neg)],
    labels=['Positive', 'Negative'],
    autopct='%1.1f%%',
    shadow=True,
    startangle=90
)
plt.axis('equal')
plt.show()

print('\033[92m' + all_pos[random.randint(0, 5000)])
print('\033[91m' + all_neg[random.randint(0, 5000)])

tweet = all_pos[random.randint(0, 5000)]
print('\033[92m' + tweet + '\033[94m')

tweet = re.sub(r'^RT[\s]+', '', tweet)
tweet = re.sub(r'https?://[^\s\n\r]+', '', tweet)
tweet = re.sub(r'#', '', tweet)
print(tweet)

tokenizer = TweetTokenizer(preserve_case=False, strip_handles=True, reduce_len=True)
tokens = tokenizer.tokenize(tweet)
print('\nTokenized:', tokens)

stop_words = stopwords.words('english')
clean_tweet = [w for w in tokens if w not in stop_words and w not in string.punctuation]
print('Cleaned tokens:', clean_tweet)

def build_freqs(tweets, labels):
    freqs = {}
    for y, tweet in zip(labels, tweets):
        for word in TweetTokenizer(preserve_case=False, strip_handles=True).tokenize(tweet):
            pair = (word, int(y))
            freqs[pair] = freqs.get(pair, 0) + 1
    return freqs

labels = np.append(np.ones(len(all_pos)), np.zeros(len(all_neg)))
freqs = build_freqs(tweets, labels)

print(f'type(freqs) = {type(freqs)}')
print(f'len(freqs) = {len(freqs)}')

keys = ['happi', 'merri', 'nice', 'good', 'bad', 'sad', 'mad', 'best', 'pretti',
        '❤', ':)', ':(', '😒', '😬', '😄', '😍', '♛', 'song', 'idea', 'power', 'play', 'magnific']

data = []
for word in keys:
    pos = freqs.get((word, 1), 0)
    neg = freqs.get((word, 0), 0)
    data.append([word, pos, neg])

fig, ax = plt.subplots(figsize=(8, 8))
x = np.log([d[1] + 1 for d in data])
y = np.log([d[2] + 1 for d in data])
ax.scatter(x, y)
plt.xlabel("Log Positive count")
plt.ylabel("Log Negative count")

for i, (word, _, _) in enumerate(data):
    ax.annotate(word, (x[i], y[i]), fontsize=12)

ax.plot([0, 9], [0, 9], color='red')
plt.show()
