# backend/utils.py
# Helper functions for generating datasets for benchmarking.
# NO CHANGES NEEDED from the Flask version.

import random

def generate_array(size, data_type="random"):
    """
    Generates an array of a given size and type.

    Args:
        size (int): The number of elements in the array.
        data_type (str): The type of data to generate.
            One of "random", "sorted", "reverse", "nearly-sorted".

    Returns:
        list: The generated list of integers.
    """
    max_val = size * 2  # Keep values in a reasonable range

    if data_type == "random":
        return [random.randint(1, max_val) for _ in range(size)]
    
    if data_type == "sorted":
        return list(range(1, size + 1))
        
    if data_type == "reverse":
        return list(range(size, 0, -1))

    if data_type == "nearly-sorted":
        arr = list(range(1, size + 1))
        # Introduce a small number of swaps to make it "nearly" sorted
        for _ in range(size // 10):  # Swap 10% of elements
            i = random.randint(0, size - 1)
            j = random.randint(0, size - 1)
            arr[i], arr[j] = arr[j], arr[i]
        return arr
        
    raise ValueError("Invalid data_type specified")