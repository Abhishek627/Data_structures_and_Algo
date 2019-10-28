'''
Find max sum subarray s.t. each subarray sum <=k
https://www.geeksforgeeks.org/maximum-subarray-size-subarrays-size-sum-less-k/
'''


def bsearch(prefix_arr, n, k):
    ans, left,right= -1,1,n

    while left<=right:
        mid = (left+right)/2





def maxSize(arr, k):
    '''
    We can do binary search on array size[1...n] and create prefix sum for each
    :param arr:
    :param k:
    :return:
    '''
    n = len(arr)

    prefix_sum = [0] * (n + 1)
    for idx, val in enumerate(arr):
        prefix_sum[idx + 1] = prefix_sum[idx] + val

    return bsearch(prefix_sum, n, k)


if __name__ == '__main__':
    arr = [1, 2, 10, 4]
    k = 14
    print maxSize(arr, k)
