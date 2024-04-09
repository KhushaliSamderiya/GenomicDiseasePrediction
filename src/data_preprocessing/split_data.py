from sklearn.model_selection import train_test_split

def stratified_split(data, labels, test_size=0.2, random_state=None):
    """
    Split the dataset into training and testing sets using stratified sampling.

    Parameters:
    data (DataFrame or ndarray): The features of your dataset.
    labels (Series or ndarray): The target variable of your dataset.
    test_size (float or int): If float, should be between 0.0 and 1.0 and represent the proportion of the dataset to include in the test split. If int, represents the absolute number of test samples.
    random_state (int): Controls the shuffling applied to the data before applying the split. Pass an int for reproducible output across multiple function calls.

    Returns:
    X_train, X_test, y_train, y_test: Features and labels split into training and testing sets.
    """
    X_train, X_test, y_train, y_test = train_test_split(data, labels, test_size=test_size, stratify=labels, random_state=random_state)
    return X_train, X_test, y_train, y_test

# Example usage
if __name__ == "__main__":
    # Assuming 'df' is your DataFrame containing features and 'labels' is a Series containing your target variable
    import pandas as pd
    import numpy as np

    # Example data
    df = pd.DataFrame({
        'Feature1': np.random.randn(100),
        'Feature2': np.random.rand(100),
        'Feature3': np.random.randint(0, 100, 100)
    })
    labels = np.random.choice([0, 1], size=100, p=[0.7, 0.3])  # Example binary target with imbalanced classes

    # Splitting the data
    X_train, X_test, y_train, y_test = stratified_split(df, labels, test_size=0.25, random_state=42)

    print("Training set size:", X_train.shape[0])
    print("Test set size:", X_test.shape[0])
    print("Training set label distribution:\n", pd.Series(y_train).value_counts(normalize=True))
    print("Test set label distribution:\n", pd.Series(y_test).value_counts(normalize=True))
