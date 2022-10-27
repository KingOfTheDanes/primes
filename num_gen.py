import random

def my_timer(orig_func):
    import time
    
    def wrapper(*args, **kwargs):
        t1 = time.time() #records time before funciton runs as t1
        result = orig_func(*args, **kwargs) #runs the decorated function
        t2 = time.time() - t1 #records time after function runs and calculates differenc from t1
        print(f'{orig_func.__name__} ran in {t2} seconds')
        return result #need return the result of the original function
    
    return wrapper #return the unexecuted wrapper to add functionality

def get_num():
    '''generate a random integer between the selected range'''
    return random.randint(100_000, 1_100_000)

def test_num(number):
    '''return Bol True if the number passed to it is prime'''
    is_prime = True
    for i in range(2, number):
        if number % i == 0:
            is_prime = False
    return is_prime

def get_prime():
    have_prime = False
    while have_prime == False:
        number = get_num()
        result = test_num(number)
        if result == True:
            break
    return number

#when theres a tricky problem, the solution is to do it more simply, not more complex
#break the problem down into little pieces, solve them individually