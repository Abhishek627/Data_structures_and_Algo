'''
Equilibrium point is index in array for which left and right subarray sum is equal
'''


def equilibrium_point(arr):
    arr_sum = sum(arr)
    left_sum = 0
    for idx, val in enumerate(arr):
        arr_sum -= val
        if left_sum == arr_sum:
            print idx
        left_sum += val
    return -1


if __name__ == '__main__':
    arr = [-7, 1, 5, 2, -4, 3, 0]
    equilibrium_point(arr)

    arr= [1,2,3,4,5]
    print equilibrium_point(arr)
