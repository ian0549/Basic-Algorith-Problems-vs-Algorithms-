
import math

def sqrt(number=None):
    """
    Calculate the floored square root of a number

    Args:
       number(int): Number to find the floored squared root
    Returns:
       int: Floored Square Root
    """
    #base code
    if number == None:
        return None

    if number < 0:
        return print('this computes square root for positive numbers only' )


    if  number == 0:
        return 0
    if number == 1:
        return 1


    min_number = 0
    max_number = number
    return square_root(number, min_number, max_number)


def square_root(number, min_number, max_number):
    """Find the mid value, multipty it by itself and comapre to number
       if it matches, then return else, if it is greter or less,
       then recurse the function by changing the min and max number wiht the mid value

    """
    # find the mid
    mid_number = (min_number +  max_number) / 2

    # if the sqaure of the mid is eqal to the number,
    # return the number else recurse if it is greater or not
    if (mid_number * mid_number) == number:
        return mid_number // 1.0
    elif (mid_number * mid_number) > number:
        return square_root(number, min_number, mid_number)
    else:
        return square_root(number, mid_number, max_number)


""" 
TESTS
"""

print ("Pass" if  (3 == sqrt(9)) else "Fail")
print ("Pass" if  (0 == sqrt(0)) else "Fail")
print ("Pass" if  (4 == sqrt(16)) else "Fail")
print ("Pass" if  (1 == sqrt(1)) else "Fail")
print ("Pass" if  (5 == sqrt(27)) else "Fail")


#test 1 when we have a negative number

print(sqrt(-1))              # should not compute 

# when we have a null input
print(sqrt() )              # returns None



print ("Pass" if  (5 == sqrt(25)) else "Fail")

print ("Pass" if  (3 == sqrt(9)) else "Fail")

print ("Pass" if  (4 == sqrt(16)) else "Fail")

print ("Pass" if  (24 == sqrt(624)) else "Fail")
print ("Pass" if  (31 == sqrt(1000)) else "Fail")

#very large input

print ("Pass" if  (sqrt(100000000000000000000) == 10000000000.0 ) else "Fail")
