import numpy as np


def train(data_array, labels):
    num_samples = normalized_data.shape[0]
    num_features = normalized_data.shape[1]
    weights = np.zeros(num_features)
    weights = np.random.rand(num_features)
    return weights


def test(test_spectrum, weights):
    score = np.dot(test_spectrum, weights)
    if score > 0.5:
        return "Type A"
    return "Type B"


return result