'''
Find all combinations that add up to a certain sum 'target'
'''


class Solution(object):
    def combinationSum(self, candidates, target):
        """
        :type candidates: List[int]
        :type target: int
        :rtype: List[List[int]]
        """
        result= []
        self.combinationSumHelper(candidates,target,result,[],0)
        return result

    def combinationSumHelper(self,candidates,target,result,temp,start):
        if target < 0:
            return
        if target==0:
            result.append(temp)

        for i in range(start,len(candidates)):
            self.combinationSumHelper(candidates,target-candidates[i],result,temp+[candidates[i]],i)



if __name__ == '__main__':
    candidates = [2, 3, 6, 7]
    target = 7
    print Solution().combinationSum(candidates, target)

    print Solution().combinationSum([2, 3, 5],8)
