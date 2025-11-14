# 🔍 Sentimental-Analysis (Naive_Bayes Branch)

This branch implements a sentiment analysis pipeline using the Naive Bayes algorithm. It covers feature creation, model training, and unit testing.

## Branch Structure

```
/ (root)
├── bayes_features/           # directory containing processed feature files
│   └── bayes_features.csv    # ready-to-use features for model training
├── create_bayes_features.py  # script to extract features from raw text
├── main1.py                  # main driver script for training & evaluating the model
├── utils.py                  # helper functions used across the pipeline
└── w2_unittest.py            # unit tests validating key components
```

## Getting Started

### Prerequisites

* Python 3.7+
* Recommended libraries: `pandas`, `numpy`, `scikit-learn` (for Naive Bayes), etc.

You can install dependencies with:

```bash
pip install -r requirements.txt
```

*if a `requirements.txt` file is present.*

### Feature Extraction

Run `create_bayes_features.py` to process raw text data and generate the feature file `bayes_features.csv`.
This step handles tasks such as tokenization, vectorization (e.g., bag-of-words, TF-IDF), and label assignment.

### Model Training & Evaluation

Run `main1.py` to train the Naive Bayes classifier on the `bayes_features.csv`. The script performs:

* model fitting
* performance evaluation (accuracy, confusion matrix, etc.)
* saving or reporting model results

### Unit Testing

Run `w2_unittest.py` to verify that key functions (in `utils.py` and elsewhere) behave as expected. Good practice before making changes.

## Example Usage

```bash
python create_bayes_features.py  # creates features
python main1.py                  # trains & evaluates model
python w2_unittest.py            # run tests
```

## Notes & Tips

* Ensure all text data is cleaned (lowercased, punctuation removed) before feature extraction.
* You can tweak feature types (unigrams, bigrams, TF-IDF thresholds) inside `create_bayes_features.py`.
* `main1.py` may be adapted to use cross-validation or parameter tuning for the Naive Bayes classifier.
* `utils.py` contains reusable functions — if you change them, always re-run unit tests.
* Always commit changes on this branch only if they relate to the Naive Bayes pipeline (so maintaining branch clarity).

## About

This branch focuses on applying a classical machine learning method (Naive Bayes) for sentiment classification. It's designed to be clear, replicable and modular — ideal for exploration, teaching, or extension into more advanced methods later.
