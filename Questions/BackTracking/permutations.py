'''
Given a list, generate all the permutations of the list
'''


class Solution(object):
    def permute(self, nums):
        """
        :type nums: List[int]
        :rtype: List[List[int]]
        """
        result = []
        self.permute_helper(nums, result, [])
        return result

    def permute_helper(self, nums, result, temp):
        if len(temp) == len(nums):
            result.append(temp)
        else:
            for i in xrange(0, len(nums)):
                if nums[i] in temp:
                    continue
                self.permute_helper(nums, result, temp + [nums[i]])



if __name__ == '__main__':
    s = Solution()
    import itertools

    nums = [1, 2, 3]
    print list(itertools.permutations(nums))
    print s.permute(nums)
