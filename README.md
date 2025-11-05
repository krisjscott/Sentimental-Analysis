```markdown
# Twitter Sentiment Analysis using NLTK

This project demonstrates how to analyze and visualize the sentiment of tweets using **NLTK (Natural Language Toolkit)**.  
It loads a built-in Twitter dataset, cleans and tokenizes text, removes noise, and visualizes word frequencies and sentiment distribution.

---

## 🧠 Overview

The goal is to understand how positive and negative tweets differ linguistically.  
We use NLTK’s pre-labeled **`twitter_samples`** dataset containing 5,000 positive and 5,000 negative tweets.

The workflow includes:
1. Loading and preparing the dataset  
2. Cleaning tweets (removing URLs, hashtags, and symbols)  
3. Tokenizing and filtering out stopwords  
4. Building word frequency dictionaries  
5. Visualizing tweet sentiment distribution and word polarity

---

## 📊 Expected Outputs

### 1. Dataset Summary
Displays the total number of tweets used for training.
```

Number of tweets: 8000

```

### 2. Sentiment Distribution Pie Chart  
 
`![Sentiment Pie Chart](images/pie_chart.png)`

A pie chart showing:
- Positive tweets: 50%  
- Negative tweets: 50%

---

### 3. Sample Tweets  
Prints one random positive and one random negative tweet in different colors.

Example:
```

I just love life and everything in it 💕   ← positive (green)
I’m so done with today 😒                  ← negative (red)

```

---

### 4. Tweet Cleaning Process  
Demonstrates how a tweet is preprocessed.

**Before:**
```

RT @happy_user: Love this! 😍 [https://t.co/xyz123](https://t.co/xyz123)

```

**After:**
```

Love this! 😍

```

*(Add image or console screenshot here)*  
`![Tweet Cleaning](images/tweet_cleaning.png)`

---

### 5. Tokenization & Stopword Removal  
Shows how text is broken into words (tokens) and filtered for meaning.

**Example:**
```

Tokenized: ['love', 'this', '😍']
Cleaned tokens: ['love', '😍']

```

---

### 6. Frequency Table Summary
Prints:
```

type(freqs) = <class 'dict'>
len(freqs) = 53858

````
This dictionary stores how often each word appears in positive vs. negative tweets.

---

### 7. Word Sentiment Scatter Plot  
*(Add scatter plot here)*  
`![Word Sentiment Plot](images/word_sentiment.png)`

A log-scale scatter plot that compares positive and negative word counts:
- Words like *happy* and *love* cluster near the **positive** side  
- Words like *sad* and *bad* cluster near the **negative** side  
- A red line separates the two sentiment regions  

---

## 🧩 Requirements

- Python 3.8+
- NLTK
- NumPy
- Matplotlib

Install dependencies:
```bash
pip install nltk numpy matplotlib
````

---

## 🚀 How to Run

1. Clone or download this project
2. Run the Python script:

   ```bash
   python main.py
   ```
3. The program will:

   * Download NLTK datasets (first time only)
   * Print summary info and cleaned tweets
   * Display two visualizations

---

## 📁 Folder Structure

```
tweets/
│
├── main.py
├── README.md
└── images/
    ├── pie_chart.png
    ├── tweet_cleaning.png
    └── word_sentiment.png
```

---

## 💡 Notes

* Each run will show different random tweets.
* The charts use logarithmic scales to make differences clearer.
* You can adjust the `keys` list in the script to analyze specific words.

---

### 🖼️ Suggested Places for Images:

* `images/pie_chart.png` → Sentiment distribution
* `images/tweet_cleaning.png` → Cleaning demo
* `images/word_sentiment.png` → Scatter plot

---

**Author:** Krish J. Scott
**Library Used:** [NLTK](https://www.nltk.org/)

```

---

Would you like me to format this README with your GitHub repo name and short project tagline at the top (like a header and short description line)? It’ll make it look even more polished for your profile.
```
