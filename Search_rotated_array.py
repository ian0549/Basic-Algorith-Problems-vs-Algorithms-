def rotated_array_search(input_list, number):

    """
    Find the index by searching in a rotated sorted array

    Args:
       input_list(array), number(int): Input array to search and the target
    Returns:
       int: Index or -1
    """
    # base cases
    if input_list == None or number == None:
        return -1
    #Empty List
    if input_list == [] or number == None:
        return -1

    start_index = 0
    end_index = len(input_list) - 1

    # get the pivot index from the list
    pivot = get_pivot(input_list, start_index, end_index)

    # select up to pivot index and perform binary search
    searched_value = binary_search(input_list[0:pivot],number )
    if searched_value != -1:
        return searched_value
    
    searched_value = binary_search(input_list[pivot: len(input_list)],number )
    if searched_value != -1:
        return searched_value + pivot

    return -1
    



def binary_search(input_list,number):
    start_index, end_index = 0, len(input_list)
    while start_index < end_index:
        offset = start_index + end_index >> 1
        if input_list[offset] < number:
            start_index = offset + 1
        elif input_list[offset] > number:
            end_index = offset
        else:
            return offset
    return -1


def get_pivot(input_list, start_index, end_index):
    middle_index = (start_index + end_index) // 2

    if input_list[start_index] <= input_list[end_index]:
        return start_index
    elif input_list[start_index] <= input_list[middle_index]:
        return get_pivot(input_list, middle_index + 1, end_index)
    else:
        return get_pivot(input_list, start_index, middle_index)

    return start_index



def linear_search(input_list, number):
    for index, element in enumerate(input_list):
        if element == number:
            return index
    return -1

def test_function(test_case):
    
    input_list = test_case[0]
    number = test_case[1]
    if linear_search(input_list, number) == rotated_array_search(input_list, number):
        print("Pass")
    else:
        print("Fail")




"""
TEST
""" 
test_function([[6, 7, 8, 9, 10, 1, 2, 3, 4], 6])
test_function([[6, 7, 8, 9, 10, 1, 2, 3, 4], 1])
test_function([[6, 7, 8, 1, 2, 3, 4], 8])
test_function([[6, 7, 8, 1, 2, 3, 4], 1])
test_function([[6, 7, 8, 1, 2, 3, 4], 10])



test_function([[], None])#Empty List, None for number
test_function([[], 6])#Empty List
test_function([[8], 8])#Singleton List with value
test_function([[8], 7])#Singleton List without value

#More tests two element lists
test_function([[7,8], 8])
test_function([[8,5], 8])
test_function([[7,8], 9])

#Full cycle of a sorted list, value present and not present
test_function([[1, 2, 3, 4, 5], 3])
test_function([[1, 2, 3, 4, 5], 6])
test_function([[2, 3, 4, 5, 1], 3])
test_function([[2, 3, 4, 5, 1], 6])
test_function([[3, 4, 5, 1, 2], 3])
test_function([[3, 4, 5, 1, 2], 6])