from sklearn.metrics import accuracy_score, roc_auc_score

def evaluate_model(model, X_test, y_test):
    """
    Evaluate the model on the test set.

    Parameters:
    model: The trained model.
    X_test (ndarray): Test feature data.
    y_test (ndarray): Test target labels.

    Returns:
    dict: A dictionary containing various performance metrics.
    """
    predictions = model.predict(X_test)
    accuracy = accuracy_score(y_test, predictions > 0.5)  # Assuming binary classification
    auc_score = roc_auc_score(y_test, predictions)
    
    metrics = {'accuracy': accuracy, 'auc': auc_score}
    return metrics
