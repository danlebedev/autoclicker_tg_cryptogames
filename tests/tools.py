from time import time

def check_time(func, *args, iterations=1):
    time1 = time()
    for _ in range(iterations):
        func(*args)
    print(func.__name__, time() - time1)