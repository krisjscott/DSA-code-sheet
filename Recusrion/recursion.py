#a = 0 ---> 1) Start
#logic ---> 2) Code
#Terminating ---> 3) End

def factorial(n):
    if n == 0 or n == 1:
        return 1 
    fact = n * factorial(n-1)
    return fact
def fibbonaci(n):
    if n == 1 or n == 2:
        return 1
    fib = fibbonaci(n-1) + fibbonaci(n-2)
    return fib
print(factorial(5))
print(fibbonaci(7))
