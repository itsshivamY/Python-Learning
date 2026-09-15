import time

def timmer(func):
    def wrapper(*args,**kwargs):
        star = time.time()
        result = func(*args,**kwargs)
        end = time.time()
        print(f"{func.__name__} ran in {end-star} time ")
        return result
    return wrapper

@timmer
def example_function(n):
    time.sleep(n)
    
example_function(3)