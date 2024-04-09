from model_definition import build_deep_neural_network
from keras.optimizers import Adam
from sklearn.model_selection import train_test_split

def train_deep_neural_network(X, y):
    """
    Train a deep neural network on the provided data.

    Parameters:
    X (ndarray): Feature data for training.
    y (ndarray): Target labels.
    """
    X_train, X_val, y_train, y_val = train_test_split(X, y, test_size=0.2, random_state=42)
    model = build_deep_neural_network(input_shape=(X_train.shape[1],))
    model.compile(optimizer=Adam(), loss='binary_crossentropy', metrics=['accuracy'])
    model.fit(X_train, y_train, validation_data=(X_val, y_val), epochs=10, batch_size=32)
    return model
