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

def digits_sum(n):
    n = abs(n)
    if n<10:
        return n
    sum = (n%10) + digits_sum(n//10)
    return sum

def count(n):
    if n<10:
        return 1
    counter = 1 + count(n//10)
    return counter

def reverse(n):
    def fun(n,length):

        if n<10:
            return n
        last_digit=n%10
        return last_digit*(10**(length-1))+fun(n//10,length-1)
    
    number=abs(n)
    size=len(str(number))
    reversed = fun(number, size)
    return -reversed if n<0 else reversed

def palindrome_num(n):
    if n<0:
        return False
    def fn(n, length):
        if n<10:
            return n
        last_num=n%10
        return last_num*(10**(length-1))+fn(n//10,length-1)
    num = n
    # print(num)
    size=len(str(num))
    # if n<0:
    #     reversed = -fn(num,size)
    reversed = fn(num,size)
    print (reversed)
    print (n)
    return reversed == n 

def summ(array):
    def sum_of_arrays(array, length):
        if length == 1:
            return array[length-1]
        elif length == 0:
            return 0
        addition = array[length-1] + sum_of_arrays(array,length-1)
        return addition  
    
    size=len(array)
    total = sum_of_arrays(array,size)
    # print(size)
    return total

def maximum(n):
    def maxi(n,length):
        if length == 1:
           return n[len-1]
        elif length == 0:
            return 0
        value = max(n[length-1],maxi(n,length-1))
        return value

    size = len(n)
    maximum_val = maxi(n,size)
    return maximum_val 

def sorted_arr(array : list) -> bool:
    def sort_check(n,l):
        if l == 0 or l == 1:
            return True
        return sort_check(n,l-1) and n[l-2]<=n[l-1]
        
    length = len(array)
    sorted = sort_check(array, length)
    return sorted 

def target(arr, target):
    def count(arr,l):
        if l==0:
            return 0
        return count(arr,l-1) + (1 if arr[l-1] == target else 0)
    return count(arr,len(arr))
# print(factorial(5))
# print(fibbonaci(7))
# print(sum_of_first(10))
# print(power(-2,4))
# print(count_down(4))
# print(triangular_number(4))
# print(fibbonaci_vari(4))
# print(digits_sum(123))
# print(count(11))
# print(reverse(-345))
# print(palindrome_num(121))
# print(summ([]))
# print(maximum([100,240,199,348,271]))
# print(sorted_arr([1,2,3,2]))
print(target([1,2,3,2,1,5],2))
