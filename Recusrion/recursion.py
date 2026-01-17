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
def sum_of_first(value):
    sum = value
    if value == 1:
        return 1
    sum = sum + sum_of_first(value-1)
    return sum
print(factorial(5))
print(fibbonaci(7))
print(sum_of_first(10))
