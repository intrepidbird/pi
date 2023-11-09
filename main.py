import math

def get_pi_digits(x: int) -> str:
    """
    Function to return the first 'x' digits of pi.

    Parameters:
    - x: int
        The number of digits of pi to retrieve.

    Returns:
    - str:
        A string containing the first 'x' digits of pi.

    Raises:
    - ValueError:
        Raises an error if 'x' is less than or equal to zero.
    """

    # Checking if 'x' is a positive integer
    if x <= 0:
        raise ValueError("The value of 'x' should be a positive integer.")

    # Getting the value of pi with the desired number of digits
    pi = str(round(math.pi, x))

    # Returning the first 'x' digits of pi
    return pi

# Example usage of the get_pi_digits function:

try:
    # Prompting the user to enter the number of digits of pi to retrieve
    num_digits = int(input("Enter the number of digits of pi to retrieve: "))

    # Calling the get_pi_digits function to retrieve the first 'num_digits' digits of pi
    result = get_pi_digits(num_digits)

    # Printing the result
    print(f"The first {num_digits} digits of pi are: {result}")
except ValueError as e:
    print(f"Error: {e}")
