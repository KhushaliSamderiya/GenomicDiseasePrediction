from sklearn.preprocessing import StandardScaler, MinMaxScaler, RobustScaler
import pandas as pd

def standard_scale(data, columns):
    """
    Apply standard scaling (z-score normalization) to specified columns.

    Parameters:
    data (DataFrame): The pandas DataFrame containing the data.
    columns (list): List of column names to be scaled.

    Returns:
    DataFrame: The DataFrame with the specified columns scaled.
    """
    scaler = StandardScaler()
    data[columns] = scaler.fit_transform(data[columns])
    return data

def min_max_scale(data, columns):
    """
    Apply Min-Max scaling to specified columns, scaling each feature to a given range, typically [0, 1].

    Parameters:
    data (DataFrame): The pandas DataFrame containing the data.
    columns (list): List of column names to be scaled.

    Returns:
    DataFrame: The DataFrame with the specified columns scaled to the range [0, 1].
    """
    scaler = MinMaxScaler()
    data[columns] = scaler.fit_transform(data[columns])
    return data

def robust_scale(data, columns):
    """
    Apply robust scaling to specified columns, scaling using statistics that are robust to outliers.

    Parameters:
    data (DataFrame): The pandas DataFrame containing the data.
    columns (list): List of column names to be scaled.

    Returns:
    DataFrame: The DataFrame with the specified columns scaled using the median and the interquartile range, thus making it more robust to outliers.
    """
    scaler = RobustScaler()
    data[columns] = scaler.fit_transform(data[columns])
    return data

# Example usage
if __name__ == "__main__":
    # Sample DataFrame
    df = pd.DataFrame({
        'Gene_Expression_A': [10, 200, 15, 20, 25],
        'Gene_Expression_B': [100, 150, 200, 250, 300],
        'Age': [20, 25, 30, 35, 40]
    })

    # Standard scaling
    df_standard_scaled = standard_scale(df.copy(), ['Gene_Expression_A', 'Gene_Expression_B'])

    # Min-Max scaling
    df_min_max_scaled = min_max_scale(df.copy(), ['Gene_Expression_A', 'Gene_Expression_B'])

    # Robust scaling
    df_robust_scaled = robust_scale(df.copy(), ['Gene_Expression_A', 'Gene_Expression_B'])

    print("Standard Scaled:\n", df_standard_scaled)
    print("\nMin-Max Scaled:\n", df_min_max_scaled)
    print("\nRobust Scaled:\n", df_robust_scaled)
