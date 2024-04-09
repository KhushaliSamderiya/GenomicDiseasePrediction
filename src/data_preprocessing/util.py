import numpy as np

def one_hot_encode_dna(sequence):
    """
    One-hot encode a DNA sequence.

    Parameters:
    sequence (str): A string representing a DNA sequence (e.g., "AGTC").

    Returns:
    ndarray: A 2D NumPy array where each row corresponds to a nucleotide and each column corresponds to a nucleotide type (A, C, G, T).
    """
    # Mapping of nucleotides to positions
    nucleotide_to_index = {'A': 0, 'C': 1, 'G': 2, 'T': 3}
    one_hot_encoded = np.zeros((len(sequence), 4))

    for i, nucleotide in enumerate(sequence):
        if nucleotide in nucleotide_to_index:
            one_hot_encoded[i, nucleotide_to_index[nucleotide]] = 1

    return one_hot_encoded

def calculate_gc_content(sequence):
    """
    Calculate the GC content of a DNA sequence.

    Parameters:
    sequence (str): A string representing a DNA sequence.

    Returns:
    float: The GC content of the sequence as a percentage of the total length.
    """
    g_count = sequence.count('G')
    c_count = sequence.count('C')
    gc_content = (g_count + c_count) / len(sequence) * 100
    return gc_content

def print_sequence_statistics(sequence):
    """
    Print basic statistics for a DNA sequence.

    Parameters:
    sequence (str): A string representing a DNA sequence.
    """
    gc_content = calculate_gc_content(sequence)
    print(f"Sequence Length: {len(sequence)}")
    print(f"GC Content: {gc_content:.2f}%")

# Example usage
if __name__ == "__main__":
    dna_sequence = "AGTCAGTCAGTCAGTCTGCA"

    # One-hot encoding
    encoded_sequence = one_hot_encode_dna(dna_sequence)
    print("One-hot Encoded Sequence:\n", encoded_sequence)

    # GC content
    gc_content = calculate_gc_content(dna_sequence)
    print("GC Content:", gc_content)

    # Print sequence statistics
    print_sequence_statistics(dna_sequence)
