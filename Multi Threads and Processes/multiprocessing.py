import multiprocessing
import math
import sys
import time

# sys.set_int_max_str_digits(100000)

def compute_factorial(number):
    print(f"Computing factorial of {number}")
    result = math.factorial(number)
    print(f"Factorial of {number} is {result}")
    return result

if __name__ == "__main__":
    numbers = [5000,6000,7000,8000]
    s_time = time.time()


    with multiprocessing.Pool() as pool:
        results = pool.map(compute_factorial, numbers)

    e_time = time.time()

    print(f"The results are: {results}")
    print(f"Time taken is {e_time - s_time} seconds")