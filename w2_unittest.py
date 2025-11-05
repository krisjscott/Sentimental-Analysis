import numpy as np

def test_train_naive_bayes(train_naive_bayes, freqs, train_x, train_y):
    """
    Simple check for train_naive_bayes() implementation.
    Validates output types and reasonable values.
    """
    print("Running test for train_naive_bayes...")

    try:
        logprior, loglikelihood = train_naive_bayes(freqs, train_x, train_y)
    except Exception as e:
        print(f"❌ Function raised an error: {e}")
        return

    if not isinstance(logprior, (float, np.floating)):
        print("❌ logprior should be a float.")
        return

    if not isinstance(loglikelihood, dict):
        print("❌ loglikelihood should be a dictionary.")
        return

    if len(loglikelihood) == 0:
        print("❌ loglikelihood dictionary is empty.")
        return

    sample_words = list(loglikelihood.keys())[:5]
    print("✅ Function executed successfully.")
    print(f"   logprior (sample): {logprior:.4f}")
    print(f"   loglikelihood sample words: {sample_words}")
    print("   Total vocabulary size:", len(loglikelihood))


def test_naive_bayes_predict(naive_bayes_predict, logprior, loglikelihood):
    """
    Simple check for naive_bayes_predict() implementation.
    Ensures it returns a numeric value.
    """
    print("Running test for naive_bayes_predict...")

    tweet = "I am happy"
    try:
        p = naive_bayes_predict(tweet, logprior, loglikelihood)
    except Exception as e:
        print(f"❌ Function raised an error: {e}")
        return

    if not isinstance(p, (float, np.floating)):
        print("❌ The returned value should be a float.")
        return

    print(f"✅ Function executed successfully. Example output: {p:.4f}")
