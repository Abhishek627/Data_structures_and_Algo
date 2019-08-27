'''
Best resource for greedy stock problems
https://leetcode.com/problems/best-time-to-buy-and-sell-stock-with-transaction-fee/discuss/108870/Most-consistent-ways-of-dealing-with-the-series-of-stock-problems/111002
'''


def maxProfit_k_1(prices):
    """
    Max profit in only 1 transaction
    :type prices: List[int]
    :rtype: int
    """
    t_i10=0
    t_i11= float("-inf")
    for price in prices:
        t_i10 = max(t_i10,t_i11+price)
        t_i11= max(t_i11,-price)
    return t_i10

if __name__ == '__main__':
    prices = [7,1,5,3,6,4]
    print maxProfit_k_1(prices)