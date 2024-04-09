import pandas as pd

def load_csv_data(file_path):
    """
    Load data from a CSV file.

    Parameters:
    file_path (str): Path to the CSV file containing the data.

    Returns:
    DataFrame: A pandas DataFrame containing the loaded data.
    """
    try:
        data = pd.read_csv(file_path)
        print(f"Data loaded successfully from {file_path}")
        return data
    except Exception as e:
        print(f"An error occurred while loading the data: {e}")
        return None

def load_fasta_data(file_path):
    """
    Load genomic sequences from a FASTA file. This is a simplified example;
    for large FASTA files, consider using BioPython or similar libraries.

    Parameters:
    file_path (str): Path to the FASTA file.

    Returns:
    dict: A dictionary with sequence identifiers as keys and sequences as values.
    """
    sequences = {}
    with open(file_path, 'r') as file:
        sequence_id = ""
        sequence = ""
        for line in file:
            if line.startswith(">"):
                if sequence_id:
                    sequences[sequence_id] = sequence
                    sequence = ""
                sequence_id = line.strip()
            else:
                sequence += line.strip()
        if sequence_id:
            sequences[sequence_id] = sequence  # Add the last sequence

    print(f"Sequences loaded successfully from {file_path}")
    return sequences

# Example usage
if __name__ == "__main__":
    # Load a sample CSV data file
    csv_data = load_csv_data("path/to/your/data.csv")
    print(csv_data.head())

    # Load a sample FASTA data file
    fasta_data = load_fasta_data("path/to/your/sequences.fasta")
    print(fasta_data)  # This will print the dictionary keys and sequences
