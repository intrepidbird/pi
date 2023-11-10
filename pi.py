def print_pi_digits(x: int):
    """
    Function to print out the first 'x' digits of pi from pi.txt file.

    Parameters:
    - x: int
        The number of digits to be printed.

    Raises:
    - ValueError:
        Raises an error if 'x' is not a positive integer.

    Returns:
    - None
        The function does not return anything.
    """

    # Validating the input 'x'
    if not isinstance(x, int) or x <= 0:
        raise ValueError("The number of digits 'x' should be a positive integer.")

    # Open the pi.txt file in read mode
    with open("pi.txt", "r") as file:
        # Read the first 'x' characters from the file
        pi_digits = file.read(x)

    # Print the first 'x' digits of pi
    print(pi_digits)

# Example usage:
print_pi_digits(10)
