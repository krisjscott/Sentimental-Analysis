# 🌐 Word Embedding Analogy & PCA Visualizer

This project plays with word embeddings to see how words relate through simple math. You’ll compare words, test country–city analogies, and plot groups of words in 2D to spot patterns you can’t see by looking at raw numbers.

## ✨ What this script does

It loads a small set of word vectors and:

* checks how similar two words are
* solves analogy questions like **Athens : Greece :: Cairo : ?**
* measures how well the analogy logic works over a small capitals dataset
* uses PCA to bring high-dimensional vectors down to 2D
* plots selected words so you can see how they group

It’s a short script, but it gives a clear feel for how these embeddings behave.

## 📁 Folder Setup

Your project should have a layout like:

```
project/
│   main.py
└── data/
       capitals.txt
       word_embeddings_subset.p
```

## ▶️ How to run

Just run:

```bash
python main.py
```

The script prints similarity scores, analogy predictions, overall accuracy, and finally opens a PCA scatter plot showing the selected words.

## 📦 Requirements

You’ll need:

* numpy
* pandas
* matplotlib

Install them with:

```bash
pip install numpy pandas matplotlib
```

## 📝 What the PCA plot tells you

The scatter plot gives a rough idea of how words cluster. Words tied to feelings, geography, and energy terms sit in their own neighborhoods. PCA compresses many dimensions into two, so the plot won’t be perfect, but it’s a helpful mental map.

## 💡 Why this project is fun

Word embeddings hide patterns in plain sight. Simple vector arithmetic captures relationships like **king → queen** or **city → country**. This script shows those patterns clearly without getting too heavy.

---

