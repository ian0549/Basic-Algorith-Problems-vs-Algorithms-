"""
Max and Min in a Unsorted Array
In this problem, we will look for smallest and largest integer from a list of unsorted integers. 
The code should run in O(n) time. 
Do not use Python's inbuilt functions to find min and max.

"""
def get_min_max(ints):
    """
    Return a tuple(min, max) out of list of unsorted integers.

    Args:
       ints(list): list of integers containing one or more integers
    """
    if ints == None or len(ints) == 0:
        return None

    if len(ints) == 1:
        return (ints[0],ints[0])
    
    # set init min an max values
    max_value = ints[0]
    min_value = ints[0]

    # iterate through the list and comapre, then set min,max values
    for i in range(1, len(ints)):
        if ints[i] > max_value:
            max_value = ints[i]
        if ints[i] < min_value:
            min_value = ints[i]

    return (min_value,max_value)


"""
Example Test Case of Ten Integers
"""
import random

l = [i for i in range(0, 10)]  # a list containing 0 - 9
random.shuffle(l)
print(l)
print ("Pass" if ((0, 9) == get_min_max(l)) else "Fail")


"""
 empty list
"""
l = [i for i in range(0, 0)] 
random.shuffle(l)
print ("Pass" if (None == get_min_max(l)) else "Fail")

"""
Null Input
"""
l = None
print ("Pass" if (None == get_min_max(l)) else "Fail")


"""
Example Test Case of 1,000,000 Integers
"""
l = [i for i in range(0, 1000000)]  
random.shuffle(l)

print ("Pass" if ((0, 999999) == get_min_max(l)) else "Fail")


"""
Example Test Case of 100,000 Integers
"""
l = [i for i in range(0, 100000)] 
random.shuffle(l)

print ("Pass" if ((0, 99999) == get_min_max(l)) else "Fail")
