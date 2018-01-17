# Prime Number Multiplication Table (Python)

## Description

This program prints out a multiplication table of the first N prime numbers. N is defaulted to 10, but can be changed by editing the "NUMBER_OF_PRIMES" variable in the prime_number_multiplication_table.py file.

## Function Descriptions
* _is_prime_ has logrithmic runtime. Given a number, it returns a boolean T/F indicating if it's prime or not. It throws an exception if the number is not valid. 
* _generate_primes_ has linear runtime. Given a number of primes to generate, it returns a list of that many prime numbers. It throws an exception if the number given is not valid.
* _generate_multiplication_table_ has quadratic runtime, as it's focused on readability rather than runtime (as a table with 10,000+ rows would be unreadable). If I needed to optimize this function, I'd consider using the numpy library to calculate and store the results as a matrix. Instead, I used the prettytable library to make the table look nice.

## How to Run Prime Number Multiplication Table

* Git clone into a new folder
* Set up a virtual environment (e.g. `virtualenv env`)
* Activate it (e.g. `source env/bin/activate`)
* Install all requirements (`pip install -r requirements.txt`)
* Run `python tests.py` (runs unit tests)
* Run `python prime_number_multiplication_table.py` (prints a multiplication table)
