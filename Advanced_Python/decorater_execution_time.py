import functools
import time

class DecoraterBasedExecutionTime:
    def __init__(self):
        pass
    
    @staticmethod
    def log_execution_time(func):
        @functools.wraps(func)
        def wrapper(*args, **kargs):
            start_time = time.time()
            result = func(*args, **kargs)
            end_time = time.time()
            execution_time = end_time - start_time
            print(f"{func.__name__} executed in {execution_time:.4f} seconds")
            return result
        return wrapper
    
    
    @log_execution_time
    def a_simple_function(self,n):
        total = sum(range(n))
        return total
    
if __name__ == "__main__" :
    obj = DecoraterBasedExecutionTime()
    result = obj.a_simple_function(100000000)
    print(result)
            
        

