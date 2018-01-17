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

## Sample Output (N = 10)

```
+--------+----+----+-----+-----+-----+-----+-----+-----+-----+-----+
| Number | 2  | 3  |  5  |  7  |  11 |  13 |  17 |  19 |  23 |  29 |
+--------+----+----+-----+-----+-----+-----+-----+-----+-----+-----+
|   2    | 4  | 6  |  10 |  14 |  22 |  26 |  34 |  38 |  46 |  58 |
|   3    | 6  | 9  |  15 |  21 |  33 |  39 |  51 |  57 |  69 |  87 |
|   5    | 10 | 15 |  25 |  35 |  55 |  65 |  85 |  95 | 115 | 145 |
|   7    | 14 | 21 |  35 |  49 |  77 |  91 | 119 | 133 | 161 | 203 |
|   11   | 22 | 33 |  55 |  77 | 121 | 143 | 187 | 209 | 253 | 319 |
|   13   | 26 | 39 |  65 |  91 | 143 | 169 | 221 | 247 | 299 | 377 |
|   17   | 34 | 51 |  85 | 119 | 187 | 221 | 289 | 323 | 391 | 493 |
|   19   | 38 | 57 |  95 | 133 | 209 | 247 | 323 | 361 | 437 | 551 |
|   23   | 46 | 69 | 115 | 161 | 253 | 299 | 391 | 437 | 529 | 667 |
|   29   | 58 | 87 | 145 | 203 | 319 | 377 | 493 | 551 | 667 | 841 |
+--------+----+----+-----+-----+-----+-----+-----+-----+-----+-----+
```
