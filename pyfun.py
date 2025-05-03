def calculate(*args, **kwargs):
    """
    Performs calculations on given numbers based on specified operations.

    Parameters:
    - *args: Numbers to operate on.
    - **kwargs: Operation flags (e.g., add=True, multiply=True).

    Returns:
    - dict: Results of requested operations.

    Raises:
    - TypeError: If non-numeric values are passed as positional arguments.
    - ValueError: If no operations are provided.
    """
    
    # Validate input types
    if not all(isinstance(num, (int, float)) for num in args):
        raise TypeError("All positional arguments must be numbers.")

    if not any(kwargs.values()):
        raise ValueError("At least one operation must be True.")

    results = {}

    # Add
    if kwargs.get('add'):
        results['add'] = sum(args)

    # Subtract
    if kwargs.get('subtract'):
        results['subtract'] = args[0] - sum(args[1:])

    # Multiply
    if kwargs.get('multiply'):
        result = 1
        for num in args:
            result *= num
        results['multiply'] = result

    # Divide
    if kwargs.get('divide'):
        try:
            result = args[0]
            for num in args[1:]:
                result /= num
            results['divide'] = result
        except ZeroDivisionError:
            results['divide'] = "Error: Division by zero"
    
    return results

# Example usage
if __name__ == "__main__":
    print(calculate(10, 2, add=True, multiply=True))  # {'add': 12, 'multiply': 20}
    print(calculate(20, 5, subtract=True, divide=True))  # {'subtract': 15, 'divide': 4.0}
