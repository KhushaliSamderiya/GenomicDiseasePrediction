import pandas as pd
from sklearn.feature_selection import RFE
from sklearn.ensemble import RandomForestClassifier
import numpy as np

def select_features_correlation(data, threshold=0.8):
    """
    Select features based on correlation threshold. Features with a correlation
    higher than the threshold to any other feature will be removed.

    Parameters:
    data (DataFrame): The pandas DataFrame containing the features.
    threshold (float): The correlation threshold to be used for feature selection.

    Returns:
    DataFrame: The DataFrame with selected features.
    """
    # Calculate the correlation matrix
    corr_matrix = data.corr().abs()

    # Select upper triangle of correlation matrix
    upper = corr_matrix.where(np.triu(np.ones(corr_matrix.shape), k=1).astype(bool))

    # Find features with correlation greater than the threshold
    to_drop = [column for column in upper.columns if any(upper[column] > threshold)]

    # Drop features
    reduced_data = data.drop(to_drop, axis=1)

    return reduced_data

def select_features_rfe(data, labels, n_features_to_select=10):
    """
    Select features using Recursive Feature Elimination (RFE).

    Parameters:
    data (DataFrame): The pandas DataFrame containing the features.
    labels (Series): The pandas Series containing the target variable.
    n_features_to_select (int): The number of features to select.

    Returns:
    DataFrame: The DataFrame with selected features.
    """
    # Initialize the model and RFE
    model = RandomForestClassifier()
    rfe = RFE(estimator=model, n_features_to_select=n_features_to_select)

    # Fit RFE
    fit = rfe.fit(data, labels)

    # Select features based on RFE support
    selected_features = data.columns[fit.support_]

    # Return reduced dataset
    reduced_data = data[selected_features]

    return reduced_data

# Example usage
if __name__ == "__main__":
    # Sample DataFrame (features) and target labels
    df = pd.DataFrame({
        'Gene_Expression_A': np.random.rand(100),
        'Gene_Expression_B': np.random.rand(100) * 0.5,
        'Gene_Expression_C': np.random.rand(100) * 1.5,
        'Gene_Expression_D': np.random.rand(100),
        'Gene_Expression_E': np.random.rand(100),
    })

    labels = np.random.randint(0, 2, size=100)  # Binary target for example

    # Feature selection using correlation
    df_selected_corr = select_features_correlation(df, threshold=0.8)
    print("Selected features based on correlation:", df_selected_corr.columns.tolist())

    # Feature selection using RFE
    df_selected_rfe = select_features_rfe(df, labels, n_features_to_select=3)
    print("Selected features using RFE:", df_selected_rfe.columns.tolist())
