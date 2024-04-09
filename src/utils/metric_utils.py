from sklearn.metrics import precision_recall_curve, auc

def calculate_auprc(y_true, y_scores):
    """
    Calculate the Area Under the Precision-Recall Curve (AUPRC).

    Parameters:
    y_true (array-like): True binary labels.
    y_scores (array-like): Target scores, can either be probability estimates of the positive class, confidence values, or non-thresholded measure of decisions.

    Returns:
    float: The AUPRC score.
    """
    precision, recall, _ = precision_recall_curve(y_true, y_scores)
    return auc(recall, precision)
