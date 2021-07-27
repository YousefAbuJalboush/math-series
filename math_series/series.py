"""
The Fibonacci Series is a numeric series starting with the integers 0 and 1. In this series, the next integer is determined by summing the previous two
"""
def fibonacci(n):
    if type(n) != int:
        return ("Invalid Input")
    elif n < 0:
        return ("Invalid Negative Value")
    elif n <= 1:
       return (n)
    else:
       return (fibonacci(n-1) + fibonacci(n-2))
        
def list_fibonacci(numbers: list) -> list: 
    return [fibonacci(num) for num in numbers]

# print(fibonacci(9))

##########################################################

"""
The Lucas Numbers are a related series of integers that start with the values 2 and 1 rather than 0 and 1.
"""
def lucas(n):
    if type(n) != int:
        return ("Invalid Input")
    elif n < 0:
        return ("Invalid Negative Value")
    elif n == 0:
       return 2
    elif n == 1:
       return 1
    else:
       return (lucas(n-1) + lucas(n-2))

def list_lucas(numbers: list) -> list: 
    return [lucas(num) for num in numbers]

# print(lucas(7))

##########################################################

"""
sum_series with one required parameter and two optional parameters. The required parameter will determine which element in the series to print. The two optional parameters will have default values of 0 and 1 and will determine the first two values for the series to be produced.
"""

def sum_series(n , first = 0 , second = 1):
    if type(n) != int:
        return ("Invalid Input")
    elif n < 0:
        return ("Invalid Negative Value")
    elif n == 0:
       return first
    elif n == 1:
       return second
    else:
       return (sum_series(n-1 , first , second ) + sum_series(n-2 , first , second ))

def list_sum_series(numbers: list , first : int , second : int) -> list: 
    return [sum_series(num , first , second ) for num in numbers]

# print(sum_series( 7 ,3 ,2))
# print(list_sum_series( [0 , 1, 2, 3, 4, 5, 6, 7] ,5 ,5 ) )