import matplotlib.pyplot as plt
import seaborn as sns

def plot_learning_curve(history, title='Model Learning Curve'):
    """
    Plot the learning curve from the training history of a model.

    Parameters:
    history: The history callback of a Keras model after training.
    title (str): The title of the plot.
    """
    plt.figure(figsize=(8, 4))
    plt.plot(history.history['accuracy'], label='Training Accuracy')
    plt.plot(history.history['val_accuracy'], label='Validation Accuracy')
    plt.title(title)
    plt.xlabel('Epochs')
    plt.ylabel('Accuracy')
    plt.legend()
    plt.show()
