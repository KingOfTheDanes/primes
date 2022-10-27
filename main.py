from num_gen import get_prime
from functools import wraps

def my_logger(orig_func):
    import logging
    logging.basicConfig(filename=f'{orig_func.__name__}.log', level=logging.INFO)

    @wraps(orig_func) #wrap the original function
    def wrapper(*args, **kwargs):

        results = orig_func(*args, **kwargs) #runs the decorated function wich is now my_timer(factor_prime())

        logging.info(
            f'Factor of {results[0][0]} found {results[0][1]}, in time: {results[1]}'
        )
        return 'Computations done, check logs for stats'
    
    return wrapper

def my_timer(orig_func):
    import time

    @wraps(orig_func) #wrap the original fucntion
    def wrapper(*args, **kwargs):
        t1 = time.time() #records time before funciton runs as t1
        result = orig_func(*args, **kwargs) #runs the decorated function
        t2 = time.time() - t1 #records time after function runs and calculates differenc from t1
        print(f'{orig_func.__name__} ran in {t2} seconds')
        return [result, t2] #need return the result of the original function
    
    return wrapper #return the unexecuted wrapper to add functionality

class factor():
    
    '''generate and factor large prime numbers to test local machine preformance'''

    def __init__(self):
        self.secret1 = get_prime()
        self.secret2 = get_prime()
        self.master = self.secret1 * self.secret2 #this is the number we will try to 'decode'

    @my_logger
    @my_timer
    def factor_prime(self, test):

        count = 0

        for i in range(2, test):

            remainder = test % i
            count += 1

            if count % 1000 == 0:
                print(f'{count} solutions tried so far')

            if remainder == 0:
                print (f'factor found: {i}')
                return [test, i]

test_1 = factor()
print(test_1.secret1)
print(test_1.secret2)
print(test_1.master)
print(test_1.factor_prime(test_1.master)) #factor_prime() is a class method from factor() class




