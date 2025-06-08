import cProfile

def add_two_number(num1:int , num2:int) -> int:
    return (num1 + num2)

def run_cprofile():
    return cProfile.run('add_two_number(3,5)')

if __name__ == "__main__":
    result = add_two_number(3,5)
    result1 = run_cprofile()
    print (f" the result is {result}, and the profiling result is {result1}")

