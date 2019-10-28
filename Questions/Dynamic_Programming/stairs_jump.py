'''
A child can jump either 1,2 or 3 stairs at a time. count number of ways to climb n stairs.
'''


def memoize(f):
    mem = {}

    def save(n):
        if n not in mem:
            mem[n] = f(n)
        return mem[n]

    return save


# Top down approach
@memoize
def countways(n):
    if n < 0:
        return 0
    if n == 0:
        return 1
    else:
        return countways(n - 1) + countways(n - 2) + countways(n - 3)

dp = [-1] * 20
# bottom up approach
def countBottomUp(n):
    dp[0] = 1
    dp[1] = 1
    dp[2] = 2
    for i in xrange(3, n + 1):
        dp[i] = dp[i - 1] + dp[i - 2] + dp[i - 3]
    return dp[n]


if __name__ == '__main__':
    for i in xrange(10):
        print i, countways(i), countBottomUp(i)
