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

def power(value, x):
    if value == 1 or x == 1:
        return value
    elif x == 0:
        return 1
    total = power(value,x-1)*value
    return total

def count_down(value):
    if value < 0:
        return 
    print(value)
    count_down(value-1)

def triangular_number(n):
    if n == 1:
        return 1
    total = n + triangular_number(n-1) 
    return total

def fibbonaci_vari(n):
    if n == 0:
        return 2
    elif n == 1:
        return 3
    new=fibbonaci_vari(n-1)+fibbonaci_vari(n-2)
    return new
     
    
    
print(factorial(5))
print(fibbonaci(7))
print(sum_of_first(10))
print(power(-2,4))
print(count_down(4))
print(triangular_number(4))
print(fibbonaci_vari(4))
