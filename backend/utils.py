import random

def generate_array(size, data_type="random"):
    max_val = size * 2  

    if data_type == "random":
        return [random.randint(1, max_val) for _ in range(size)]
    
    if data_type == "sorted":
        return list(range(1, size + 1))
        
    if data_type == "reverse":
        return list(range(size, 0, -1))

    if data_type == "nearly-sorted":
        arr = list(range(1, size + 1))
        for _ in range(size // 10):  # Swap 10% of elements
            i = random.randint(0, size - 1)
            j = random.randint(0, size - 1)
            arr[i], arr[j] = arr[j], arr[i]
        return arr
        
    raise ValueError("Invalid data_type specified")
