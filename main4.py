import numpy as np
import pandas as pd
import pickle
import matplotlib.pyplot as plt


def cosine_similarity(A, B):
    dot = A @ B
    norma = np.linalg.norm(A)
    normb = np.linalg.norm(B)
    return dot / (norma * normb)


def euclidean(A, B):
    return np.linalg.norm(A - B)


def get_country(city1, country1, city2, word_embeddings, cosine_similarity=cosine_similarity):
    group = (city1, country1, city2)

    c1 = word_embeddings[city1]
    k1 = word_embeddings[country1]
    c2 = word_embeddings[city2]

    vec = k1 - c1 + c2

    best_sim = -1
    best_word = ""

    for w, emb in word_embeddings.items():
        if w not in group:
            sim = cosine_similarity(vec, emb)
            if sim > best_sim:
                best_sim = sim
                best_word = w

    return best_word, best_sim


def get_accuracy(word_embeddings, data):
    correct = 0
    total = len(data)

    for _, row in data.iterrows():
        pred, _ = get_country(
            row["city1"], row["country1"], row["city2"], word_embeddings
        )
        if pred == row["country2"]:
            correct += 1

    return correct / total


def compute_pca(X, n_components=2):
    X_demeaned = X - np.mean(X, axis=0)
    cov = np.cov(X_demeaned, rowvar=False)
    eigen_vals, eigen_vecs = np.linalg.eigh(cov)

    idx = np.argsort(eigen_vals)[::-1]
    eigen_vecs_sorted = eigen_vecs[:, idx]
    subset = eigen_vecs_sorted[:, :n_components]

    return np.dot(X_demeaned, subset)


def get_vectors(word_embeddings, words):
    return np.array([word_embeddings[w] for w in words])


def main():
    print("Loading data...")
    data = pd.read_csv("./data/capitals.txt", delimiter=" ")
    data.columns = ["city1", "country1", "city2", "country2"]

    word_embeddings = pickle.load(open("./data/word_embeddings_subset.p", "rb"))
    print(f"Loaded {len(word_embeddings)} word embeddings.")

    king = word_embeddings["king"]
    queen = word_embeddings["queen"]

    print("\nCosine similarity (king, queen):", cosine_similarity(king, queen))
    print("Euclidean distance (king, queen):", euclidean(king, queen))

    example = get_country("Athens", "Greece", "Cairo", word_embeddings)
    print("\nAnalogy test (Athens:Greece :: Cairo:? ):")
    print("Predicted:", example)

    print("\nComputing accuracy...")
    acc = get_accuracy(word_embeddings, data)
    print(f"Accuracy: {acc:.2f}")

    words = [
        "oil", "gas", "happy", "sad", "city", "town",
        "village", "country", "continent", "petroleum", "joyful"
    ]

    X = get_vectors(word_embeddings, words)
    result = compute_pca(X, 2)

    plt.scatter(result[:, 0], result[:, 1])
    for i, word in enumerate(words):
        plt.annotate(word, (result[i, 0] - 0.05, result[i, 1] + 0.1))

    print("\nShowing PCA plot...")
    plt.show()


if __name__ == "__main__":
    main()
