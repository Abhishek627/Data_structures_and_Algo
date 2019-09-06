'''
https://leetcode.com/problems/super-egg-drop/
We can determine the minimum number of drops required for a floor F, depending on the answer of floors below it.
This looks like a binary search problem but K can be less too. IF k < log(N), we can't do binary search properly.
This can be solved using DP.
Let's look at creating a correct recursive formula and filling the dp table bottom up.

'''


class Solution(object):
    def superEggDrop(self, K, N):
        """
        O(k*N^2)
        :type K: int  Number of eggs
        :type N: int Number of floors
        :rtype: int
        """
        dp = [[float('inf')] * (N + 1) for _ in range(K + 1)]
        for i in range(1, K + 1):
            dp[i][0] = 0
            dp[i][1] = 1
        for j in range(1, N + 1):
            dp[1][j] = j

        for i in range(2, K + 1):
            for j in range(2, N + 1):
                for k in range(1, j + 1):
                    dp[i][j] = min(dp[i][j], 1 + max(dp[i - 1][k - 1], dp[i][j - k]))
        return dp[K][N]




if __name__ == '__main__':
    print Solution().superEggDrop(2,6)
