import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
from matplotlib.patches import Ellipse
import nltk
from nltk.corpus import stopwords, twitter_samples
from nltk.tokenize import TweetTokenizer
from os import getcwd
from utils import process_tweet, lookup
import w2_unittest

# Download necessary NLTK data
nltk.download('twitter_samples')
nltk.download('stopwords')

# -------------------------------------------------------
# Helper function: Confidence ellipse for visualization
# -------------------------------------------------------
def confidence_ellipse(x, y, ax, n_std=3.0, facecolor='none', **kwargs):
    x, y = np.asarray(x), np.asarray(y)
    if x.size != y.size:
        raise ValueError("x and y must be the same size")

    cov = np.cov(x, y)
    if cov.shape != (2, 2):
        return None

    vals, vecs = np.linalg.eigh(cov)
    order = vals.argsort()[::-1]
    vals, vecs = vals[order], vecs[:, order]
    angle = np.degrees(np.arctan2(vecs[1, 0], vecs[0, 0]))

    width, height = 2 * n_std * np.sqrt(vals)
    mean_x, mean_y = np.mean(x), np.mean(y)

    ellipse = Ellipse((mean_x, mean_y), width=width, height=height, angle=angle,
                      facecolor=facecolor, **kwargs)
    ax.add_patch(ellipse)
    return ellipse

# -------------------------------------------------------
# Load and visualize sentiment features
# -------------------------------------------------------
data = pd.read_csv('C:\\Users\\thekr\\OneDrive\\Documents\\program\\python\\tweets\\bayes_features.csv')
colors = ['red', 'green']
sentiments = ['negative', 'positive']

fig, ax = plt.subplots(figsize=(8, 8))
for sentiment in data.sentiment.unique():
    ix = data.index[data.sentiment == sentiment]
    ax.scatter(data.iloc[ix].positive, data.iloc[ix].negative,
               c=colors[int(sentiment)], s=0.1, marker='*',
               label=sentiments[int(sentiment)])

plt.xlim(-250, 0)
plt.ylim(-250, 0)
plt.xlabel("Positive")
plt.ylabel("Negative")
ax.legend(loc='best')
plt.show()

# Plot with confidence ellipses
fig, ax = plt.subplots(figsize=(8, 8))
for sentiment in data.sentiment.unique():
    ix = data.index[data.sentiment == sentiment]
    ax.scatter(data.iloc[ix].positive, data.iloc[ix].negative,
               c=colors[int(sentiment)], s=0.1, marker='*',
               label=sentiments[int(sentiment)])

plt.xlim(-200, 40)
plt.ylim(-200, 40)
plt.xlabel("Positive")
plt.ylabel("Negative")

data_pos = data[data.sentiment == 1]
data_neg = data[data.sentiment == 0]

confidence_ellipse(data_pos.positive, data_pos.negative, ax, n_std=2, edgecolor='black', label=r'$2\sigma$')
confidence_ellipse(data_neg.positive, data_neg.negative, ax, n_std=2, edgecolor='orange')
confidence_ellipse(data_pos.positive, data_pos.negative, ax, n_std=3, edgecolor='black', linestyle=':', label=r'$3\sigma$')
confidence_ellipse(data_neg.positive, data_neg.negative, ax, n_std=3, edgecolor='orange', linestyle=':')
ax.legend(loc='lower right')
plt.show()

# -------------------------------------------------------
# Modify and visualize adjusted data
# -------------------------------------------------------
data2 = data.copy()
data2.loc[data2.sentiment == 1, 'negative'] = data2.negative * 1.5 + 50
data2.loc[data2.sentiment == 1, 'positive'] = data2.positive / 1.5 - 50

fig, ax = plt.subplots(figsize=(8, 8))
for sentiment in data2.sentiment.unique():
    ix = data2.index[data2.sentiment == sentiment]
    ax.scatter(data2.iloc[ix].positive, data2.iloc[ix].negative,
               c=colors[int(sentiment)], s=0.1, marker='*',
               label=sentiments[int(sentiment)])

plt.xlim(-200, 40)
plt.ylim(-200, 40)
plt.xlabel("Positive")
plt.ylabel("Negative")

data_pos = data2[data2.sentiment == 1]
data_neg = data2[data2.sentiment == 0]

confidence_ellipse(data_pos.positive, data_pos.negative, ax, n_std=2, edgecolor='black', label=r'$2\sigma$')
confidence_ellipse(data_neg.positive, data_neg.negative, ax, n_std=2, edgecolor='orange')
confidence_ellipse(data_pos.positive, data_pos.negative, ax, n_std=3, edgecolor='black', linestyle=':', label=r'$3\sigma$')
confidence_ellipse(data_neg.positive, data_neg.negative, ax, n_std=3, edgecolor='orange', linestyle=':')
ax.legend(loc='lower right')
plt.show()

# -------------------------------------------------------
# Prepare Twitter dataset
# -------------------------------------------------------
filePath = f"{getcwd()}/../tmp2/"
nltk.data.path.append(filePath)

all_positive_tweets = twitter_samples.strings('positive_tweets.json')
all_negative_tweets = twitter_samples.strings('negative_tweets.json')

test_pos, train_pos = all_positive_tweets[4000:], all_positive_tweets[:4000]
test_neg, train_neg = all_negative_tweets[4000:], all_negative_tweets[:4000]

train_x, test_x = train_pos + train_neg, test_pos + test_neg
train_y = np.append(np.ones(len(train_pos)), np.zeros(len(train_neg)))
test_y = np.append(np.ones(len(test_pos)), np.zeros(len(test_neg)))

# -------------------------------------------------------
# Count words by sentiment
# -------------------------------------------------------
def count_tweets(result, tweets, ys):
    for y, tweet in zip(ys, tweets):
        for word in process_tweet(tweet):
            pair = (word, y)
            result[pair] = result.get(pair, 0) + 1
    return result

freqs = count_tweets({}, train_x, train_y)

# -------------------------------------------------------
# Train Naive Bayes model
# -------------------------------------------------------
def train_naive_bayes(freqs, train_x, train_y):
    loglikelihood = {}
    vocab = set([pair[0] for pair in freqs.keys()])
    V = len(vocab)

    N_pos = sum(freqs[pair] for pair in freqs if pair[1] == 1)
    N_neg = sum(freqs[pair] for pair in freqs if pair[1] == 0)

    D_pos = np.sum(train_y == 1)
    D_neg = np.sum(train_y == 0)
    logprior = np.log(D_pos / D_neg)

    for word in vocab:
        freq_pos = freqs.get((word, 1), 0)
        freq_neg = freqs.get((word, 0), 0)

        p_w_pos = (freq_pos + 1) / (N_pos + V)
        p_w_neg = (freq_neg + 1) / (N_neg + V)
        loglikelihood[word] = np.log(p_w_pos / p_w_neg)

    return logprior, loglikelihood

logprior, loglikelihood = train_naive_bayes(freqs, train_x, train_y)
w2_unittest.test_train_naive_bayes(train_naive_bayes, freqs, train_x, train_y)

# -------------------------------------------------------
# Predict sentiment using Naive Bayes
# -------------------------------------------------------
def naive_bayes_predict(tweet, logprior, loglikelihood):
    words = process_tweet(tweet)
    p = logprior
    for word in words:
        if word in loglikelihood:
            p += loglikelihood[word]
    return p

# -------------------------------------------------------
# Test model accuracy
# -------------------------------------------------------
def test_naive_bayes(test_x, test_y, logprior, loglikelihood):
    y_hats = [1 if naive_bayes_predict(t, logprior, loglikelihood) > 0 else 0 for t in test_x]
    error = np.mean(np.abs(y_hats - test_y))
    return 1 - error

print(f"Naive Bayes accuracy = {test_naive_bayes(test_x, test_y, logprior, loglikelihood):.4f}")

# -------------------------------------------------------
# Ratio analysis
# -------------------------------------------------------
def get_ratio(freqs, word):
    pos = lookup(freqs, word, 1)
    neg = lookup(freqs, word, 0)
    return {'positive': pos, 'negative': neg, 'ratio': (pos + 1) / (neg + 1)}

def get_words_by_threshold(freqs, label, threshold):
    word_list = {}
    for word, _ in freqs.keys():
        ratio = get_ratio(freqs, word)
        if (label == 1 and ratio['ratio'] >= threshold) or (label == 0 and ratio['ratio'] <= threshold):
            word_list[word] = ratio
    return word_list

# -------------------------------------------------------
# Error analysis
# -------------------------------------------------------
print('Truth\tPredicted\tTweet')
for x, y in zip(test_x, test_y):
    y_hat = naive_bayes_predict(x, logprior, loglikelihood)
    if y != (np.sign(y_hat) > 0):
        print(f'{y}\t{np.sign(y_hat) > 0}\t{" ".join(process_tweet(x)).encode("ascii", "ignore")}')

# Test your own tweet
my_tweet = 'I am happy because I am learning :)'
p = naive_bayes_predict(my_tweet, logprior, loglikelihood)
print(p)
