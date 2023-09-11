from time import time

def performance(func):
    def wrapper(*args, **kwargs):
        t1 = time()
        res = func(*args, **kwargs)
        t2 = time()
        print(f'It took {t2 - t1} seconds to run')
        return res
    return wrapper

@performance
def longfunc():
    for i in range(100000000):
        1**4

longfunc()