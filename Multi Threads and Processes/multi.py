from concurrent.futures import ThreadPoolExecutor,ProcessPoolExecutor

def print_numbers(n):
    return f"Number: {n}"

def square_num(n):
    return f"Square: {n**2}"

n = [1,2,3,0,5,7,8,16,10]

# with ThreadPoolExecutor(max_workers=3) as executor:
#     results = executor.map(print_numbers,n)

# for result in results:
#     print(result)

with ProcessPoolExecutor(max_workers=3) as pexecutor:
    res = pexecutor.map(square_num,n)

for result in res:
    print(result)