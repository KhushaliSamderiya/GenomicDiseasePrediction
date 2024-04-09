import numpy as np

def shuffle_data(data, labels):
    """
    Shuffle the data and labels in unison.

    Parameters:
    data (ndarray): The data to shuffle.
    labels (ndarray): The corresponding labels to shuffle.

    Returns:
    Tuple of ndarray: The shuffled data and labels.
    """
    assert len(data) == len(labels)
    p = np.random.permutation(len(data))
    return data[p], labels[p]
