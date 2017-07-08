cube = lambda x: x*x*x # complete the lambda function 

def fib(n):
    if(n == 0 or n == 1):
        return n
    else:
        return fib(n-1) + fib(n-2)
    

def fibonacci(n):
    # return a list of fibonacci numbers
    return [ fib(x) for x in range(n) ]
