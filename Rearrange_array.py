
"""
Rearrange Array Elements
Rearrange Array Elements so as to form two number such that their sum is maximum. 
Return these two numbers. You can assume that all array elements are in the range [0, 9]. 
The number of digits in both the numbers cannot differ by more than 1. You're not allowed to use any sorting function that Python provides and the expected time complexity is O(nlog(n)).

for e.g. [1, 2, 3, 4, 5]

The expected answer would be [531, 42].
Another expected answer can be [542, 31]. 
In scenarios such as these when there are more than one possible answers, 
return any one.

Here is some boilerplate code and test cases to start with:

"""

def mergesort(items):
    
    if len(items) <= 1:
        return items
    
    mid = len(items) // 2
    left = items[:mid]
    right = items[mid:]
    
    left = mergesort(left)
    right = mergesort(right)
    
    return merge(left, right)

def merge(left, right):

    merged = []
    left_index = 0
    right_index = 0
    
    while left_index < len(left) and right_index < len(right):
        if left[left_index] > right[right_index]:
            merged.append(right[right_index])
            right_index += 1
        else:
            merged.append(left[left_index])
            left_index += 1

    merged += left[left_index:]
    merged += right[right_index:]
        
    return merged

def rearrange_digits(input_list):
    """
    Rearrange Array Elements so as to form two number such that their sum is maximum.

    Args:
       input_list(list): Input List
    Returns:
       (int),(int): Two maximum sums
    """

    if input_list == None or len(input_list) == 0:
        return -1, -1
    if len(input_list) == 1 :
        return input_list[0], 0

    #sort elements
    sorted_list = mergesort(input_list)
    
    numer1 =""
    number2 =""
    # reverse the index list, get odd and even indexes and add to str numbers 1and 2
    for i in reversed(range(len(sorted_list))):
        if i % 2 == 0:
            numer1 += str(sorted_list[i])
        elif i % 2 == 1:
            number2 += str(sorted_list[i])
    
    return int(numer1), int(number2)


def test_function(test_case):
    output = rearrange_digits(test_case[0])
    solution = test_case[1]
    if sum(output) == sum(solution):
        print("Pass")
    else:
        print("Fail")

test_function([[1, 2, 3, 4, 5], [542, 31]])
test_case = [[4, 6, 2, 5, 9, 8], [964, 852]]




"""
Test Code
"""
test_function ([[9,9], [9, 9]])
test_function([[1,2,3,4], [42, 31]]) 
test_function([[2,2,2,2,2], [222, 22]]) 


#Null input 
test_function([None, [-1, -1]])

#Empty input    
test_function([[], [-1, -1]])    

#Single value input
test_function([[1], [1, 0]]) 

"""
Larger Inputs
"""
test_function([[9,8,7,6,5,4,3,2,1,0,0], [975310, 86420]])
test_function([[2,3,1,4,2,3,1,3,3,4,8,6,9,9,1,0,0], [984332110, 96433210]])