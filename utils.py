# utils.py
import re
import string
from nltk.corpus import stopwords
from nltk.tokenize import TweetTokenizer

def process_tweet(tweet):
    """
    Clean and tokenize a tweet.
    Steps:
    1. Lowercase
    2. Remove URLs, handles, hashtags, punctuation
    3. Remove stopwords
    4. Tokenize
    """
    stemmer = None  # not used here but can be added
    stopwords_english = stopwords.words('english')
    tokenizer = TweetTokenizer(preserve_case=False, strip_handles=True, reduce_len=True)

    # Remove URLs
    tweet = re.sub(r'https?://\S+', '', tweet)
    # Remove hashtags and handles
    tweet = re.sub(r'#', '', tweet)
    # Tokenize
    tokens = tokenizer.tokenize(tweet)

    cleaned_tweets = []
    for word in tokens:
        # Remove punctuation
        if word in string.punctuation:
            continue
        # Remove stopwords and numbers
        if word not in stopwords_english and word.isalpha():
            cleaned_tweets.append(word)
    return cleaned_tweets


def lookup(freqs, word, label):
    """
    Look up how often a word appears in the given label (0 or 1).
    """
    pair = (word, label)
    return freqs.get(pair, 0)
