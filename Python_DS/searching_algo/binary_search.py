"""
Binary search function.
Assume the list only has distinct elements,
meaning there are no repeated values, and
elements are in a strictly increasing order.
Return the index of value, or -1 if the value
doesn't exist in the list."""


def is_sorted(input_array):
    return all(input_array[i] <= input_array[i + 1] for i in xrange(len(input_array) - 1))

def binary_search_iterative(input_array, value):
    low=0
    high= len(input_array)-1
    while(low<=high):
        mid= low+ (high-low)/2
        if input_array[mid]==value:
            return mid
        elif input_array[mid]>value:
            high=mid-1
        else:
            low=mid+1
    return -1

def binary_search_recursive(input_array, value, low =0 ,high=None):
    high=len(input_array) if high is None else high
    if low>high:
        return  -1
    mid= low+ (high-low)/2
    if value<input_array[mid]:
        #go to left subarray
        return binary_search_recursive(input_array,value,low,mid-1)
    elif value>input_array[mid]:
        return binary_search_recursive(input_array,value,mid+1,high)
    else:
        return mid



if __name__ == '__main__':
    test_list = [1,3,9,11,15,19,29]
    test_val1 = 25
    test_val2 = 15

    if is_sorted(test_list):
        print "ITERATIVE RESULT"
        print binary_search_iterative(test_list, test_val1)
        print binary_search_iterative(test_list, test_val2)
        for i in test_list:
            print binary_search_iterative(test_list,i),

        print "\nRECURSIVE RESULT"
        print binary_search_recursive(test_list,test_val1)
        print binary_search_recursive(test_list,test_val2)

        for i in test_list:
            print binary_search_recursive(test_list,i),
