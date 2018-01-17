from prettytable import PrettyTable
from math import sqrt, ceil


NUMBER_OF_PRIMES = 10


def is_prime(number):
    """
    Checks if a given number is prime.

    Args:
        Number (int): Number to be checked if prime
    Returns:
        Boolean: True if the number is prime, False if it is not
    Raises:
        Exception when number is invalid.
    """
    if number < 1 or type(number) != int:
        raise Exception('Invalid number, must be a positive integer.')
    if number == 1:
        return False
    if number == 2:
        return True
    # Shortening range to keep function in log(n) time, once the square root is
    # reached, we don't need to keep checking for a prime number
    for divisor in range(2, int(ceil(sqrt(number)) + 1)):
        if (number % divisor == 0):
            # There is at least one other divisor of this number, return false
            return False
    return True


def generate_primes(num_prime):
    """
    Generate a specified number of primes and return as a list.

    Args:
        Num_prime: The number of primes you want to generate
    Returns:
        A list of prime numbers
    Raises:
        Exception when num_prime is invalid.
    """

    if num_prime < 1 or type(num_prime) != int:
        raise Exception('Invalid number, must be a positive integer.')

    prime_list = []
    i = 1
    while len(prime_list) < num_prime:
        if is_prime(i):
            prime_list.append(i)
        i += 1
    return prime_list


def generate_multiplication_table(number_list):
    """
    Generate a multiplication table from a list of numbers, using prettytable.

    Args:
        Number_list: The list of numbers to use for the multiplication table
    Returns:
        A multiplication table based on the number list provided.
    Raises:
        Exception when list contains items that are not integers.

    This function is optimized for readability rather than run time, as
    large tables would not print out nicely in terminal.
    """

    #create table and columns
    columns = ['Number'] + number_list
    t = PrettyTable(columns)
    #add rows
    for row_num in number_list:
        # multiply all numbers in the row by the row number
        try:
            multiplication_list = [col_num * row_num for col_num in number_list]
        except TypeError:
            raise Exception('Invalid list, should only contain integers.')
        row_list = [row_num] + multiplication_list
        t.add_row(row_list)
    return t

if __name__ == "__main__":
    primes = generate_primes(NUMBER_OF_PRIMES)
    print generate_multiplication_table(primes)
