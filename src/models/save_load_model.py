import joblib
from keras.models import load_model

def save_model(model, filename):
    """
    Save a trained model to disk.

    Parameters:
    model: The trained model to save.
    filename (str): The path to save the model file.
    """
    if isinstance(model, Sequential):
        model.save(filename)  # For Keras/TF models
    else:
        joblib.dump(model, filename)  # For sklearn models and others

def load_model_from_disk(filename, is_keras_model=False):
    """
    Load a trained model from disk.

    Parameters:
    filename (str): The path to the model file.
    is_keras_model (bool): Set to True if loading a Keras/TF model.

    Returns:
    The loaded model.
    """
    if is_keras_model:
        return load_model(filename)
    else:
        return joblib.load(filename)
