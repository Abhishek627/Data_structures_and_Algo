'''
https://leetcode.com/problems/relative-sort-array/
'''


class Solution(object):
    def relativeSortArray(self, arr1, arr2):
        """
        :type arr1: List[int]
        :type arr2: List[int]
        :rtype: List[int]
        """
        from collections import Counter
        result =[]
        count = Counter(arr1)
        for item in arr2:
            for i in range(count[item]):
                result.append(item)
        arr1[:] = (val for val in arr1 if val not in arr2)
        arr1.sort()
        result.extend(arr1)
        return result

    def relativeSortArrayBetter(self, A, B):
        '''
        Create a dict with val,index pair for B. Sort A according to it.
        '''
        k = {v: i for i, v in enumerate(B)}
        return sorted(A, key=lambda i: k.get(i, 1000 + i))

if __name__ == '__main__':
    arr1 = [2, 3, 1, 3, 2, 4, 6, 7, 9, 2, 19]
    arr2 = [2, 1, 4, 3, 9, 6]

    arr1= [28, 6, 22, 8, 44, 17]
    arr2= [22, 28, 8, 6]
    # print Solution().relativeSortArray(arr1,arr2)

    print Solution().relativeSortArrayBetter(arr1,arr2)

