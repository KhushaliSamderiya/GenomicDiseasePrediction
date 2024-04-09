def read_fasta_file(fasta_file):
    """
    Read a FASTA file and return a dictionary of sequences.

    Parameters:
    fasta_file (str): Path to the FASTA file.

    Returns:
    dict: A dictionary with sequence IDs as keys and sequences as values.
    """
    sequences = {}
    with open(fasta_file, 'r') as file:
        sequence_id = None
        sequence = ''
        for line in file:
            if line.startswith('>'):
                if sequence_id:
                    sequences[sequence_id] = sequence
                    sequence = ''
                sequence_id = line.strip()[1:]  # Remove '>'
            else:
                sequence += line.strip()
        if sequence_id:
            sequences[sequence_id] = sequence  # Add the last sequence
    return sequences
