from sklearn.ensemble import RandomForestClassifier
from keras.models import Sequential
from keras.layers import Dense, Dropout

def build_random_forest_classifier(n_estimators=100):
    """
    Build a Random Forest classifier.

    Parameters:
    n_estimators (int): The number of trees in the forest.

    Returns:
    RandomForestClassifier: The Random Forest model.
    """
    model = RandomForestClassifier(n_estimators=n_estimators)
    return model

def build_deep_neural_network(input_shape):
    """
    Build a simple deep neural network.

    Parameters:
    input_shape (tuple): The shape of the input data.

    Returns:
    Sequential: The deep neural network model.
    """
    model = Sequential()
    model.add(Dense(128, activation='relu', input_shape=input_shape))
    model.add(Dropout(0.5))
    model.add(Dense(64, activation='relu'))
    model.add(Dropout(0.5))
    model.add(Dense(1, activation='sigmoid'))  # Binary classification output
    return model
