def generate_fibonacci(start_sequence, length):
    """
    Generate a Fibonacci sequence of given length starting with two given numbers.
    
    Args:
        start_sequence (list): List containing two starting numbers
        length (int): Desired length of the sequence
    
    Returns:
        list: Fibonacci sequence of specified length
    """
    # Validate inputs
    if not isinstance(start_sequence, list) or len(start_sequence) != 2:
        raise ValueError("start_sequence must be a list containing exactly two numbers")
    
    if not isinstance(length, int) or length < 0:
        raise ValueError("length must be a non-negative integer")
    
    # Handle special cases
    if length == 0:
        return []
    if length == 1:
        return [start_sequence[0]]
    if length == 2:
        return start_sequence.copy()
    
    # Generate sequence
    sequence = start_sequence.copy()
    for _ in range(length - 2):
        sequence.append(sequence[-1] + sequence[-2])
    
    return sequence

# Interactive testing
if __name__ == "__main__":
    try:
        start1 = int(input("Enter the first number: "))
        start2 = int(input("Enter the second number: "))
        length = int(input("Enter the desired sequence length: "))
        
        result = generate_fibonacci([start1, start2], length)
        print(f"\nFibonacci sequence: {result}")
    except ValueError as e:
        print(f"Error: {e}")
