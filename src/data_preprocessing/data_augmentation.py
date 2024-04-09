import random

def shift_sequence(sequence, shift_range):
    """
    Shift a sequence left or right by a random number of positions within shift_range.

    Parameters:
    sequence (str): The original sequence (e.g., a DNA sequence).
    shift_range (int): The maximum number of positions to shift the sequence.

    Returns:
    str: The shifted sequence.
    """
    shift = random.randint(-shift_range, shift_range)
    if shift == 0:
        return sequence
    elif shift > 0:
        return sequence[shift:] + sequence[:shift]
    else:
        return sequence[shift:] + sequence[:shift]

def flip_sequence(sequence):
    """
    Flip a sequence, creating a mirror image of the original sequence.

    Parameters:
    sequence (str): The original sequence.

    Returns:
    str: The flipped sequence.
    """
    return sequence[::-1]

def introduce_mutation(sequence, mutation_rate=0.01):
    """
    Randomly introduce mutations into a sequence based on a mutation rate.

    Parameters:
    sequence (str): The original sequence.
    mutation_rate (float): The rate at which mutations are introduced.

    Returns:
    str: The mutated sequence.
    """
    nucleotides = ['A', 'C', 'G', 'T']
    mutated_sequence = ''
    for nucleotide in sequence:
        if random.random() < mutation_rate:
            mutated_sequence += random.choice([n for n in nucleotides if n != nucleotide])
        else:
            mutated_sequence += nucleotide
    return mutated_sequence

# Example usage
if __name__ == "__main__":
    original_sequence = "ACGTACGTACGT"

    # Shift the sequence
    shifted_sequence = shift_sequence(original_sequence, 3)
    print("Shifted Sequence:", shifted_sequence)

    # Flip the sequence
    flipped_sequence = flip_sequence(original_sequence)
    print("Flipped Sequence:", flipped_sequence)

    # Introduce mutations
    mutated_sequence = introduce_mutation(original_sequence, mutation_rate=0.05)
    print("Mutated Sequence:", mutated_sequence)
