# 🗺️ Word Embedding Analogy & PCA Visualization

This project demonstrates how to work with pre-trained word embeddings to explore word relationships, run analogy tests, measure accuracy on a capitals dataset, and visualize embedding clusters using PCA.

## Overview

The script performs the following tasks:

1. Loads a subset of pre-trained word embeddings.
2. Computes cosine similarity and Euclidean distance between word vectors.
3. Solves analogy problems using vector arithmetic
   Example: *Athens : Greece :: Cairo : ?*
4. Evaluates accuracy on a dataset of capital–country pairs.
5. Reduces embedding dimensions using PCA.
6. Visualizes selected words in 2D space with Matplotlib.

## Project Structure

```
project/
│
├── data/
│   ├── capitals.txt
│   └── word_embeddings_subset.p
│
├── main.py
└── README.md
```

## Requirements

Python 3.8+
The following libraries are needed:

* numpy
* pandas
* matplotlib
* pickle (standard library)

Install using:

```bash
pip install numpy pandas matplotlib
```

## How It Works

### Analogy Function

The analogy task uses the common vector approach:

```
vec = country1 - city1 + city2
```

The script compares this vector to all embeddings and returns the closest match by cosine similarity.

### Accuracy Check

The capitals dataset contains four columns:

```
city1 country1 city2 country2
```

For each row, the script predicts `country2` using the analogy method and reports overall accuracy.

### PCA Visualization

A small set of meaningful words is projected into 2D space using PCA.
The scatter plot helps show how related concepts cluster based on their embeddings.

## Running the Script

From the project folder:

```bash
python main.py
```

This will:

* Print similarity scores
* Run an analogy example
* Compute and print accuracy
* Show a PCA scatter plot of selected words

## Example Output (abridged)

```
Loaded 50000 word embeddings.
Cosine similarity (king, queen): 0.65123
Euclidean distance (king, queen): 3.1278

Analogy test (Athens:Greece :: Cairo:? ):
Predicted: ('Egypt', 0.6892)

Accuracy: 0.72
Showing PCA plot...
```

## Notes

* The embeddings file should be placed inside the `data/` folder.
* The capitals dataset must follow the same structure shown above.
* You can replace the word list in the PCA section to explore other semantic groups.

---

