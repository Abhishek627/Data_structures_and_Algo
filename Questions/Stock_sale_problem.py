'''

Given an array containing stock prices for a company. Give the most profit we can make by buying first and selling later only once.
'''


def get_max_profit(input_list):
    # Simple looping and comparison. Every cycle I'm comparing (n-1)+(n-2)+(n-3)+.....1 comparisons.
    # Therefore this is also O(n^2)
    max_profit = float('-inf')
    for i in xrange(len(input_list)):
        for j in input_list[i:]:
            max_profit = max(j - input_list[i], max_profit)
    return max_profit


def greedy_get_max_profit(input_list):
    # special cases: If monotonically decreasing list. What should I do ?
    if len(input_list) < 2:
        return
    min_price = input_list[0]
    max_profit = input_list[1] - input_list[0]
    for i in xrange(1, len(input_list)):
        curr_price = input_list[i]
        max_profit = max(curr_price - min_price, max_profit)
        min_price = min(min_price, curr_price)
    return max_profit


def get_max_profit_multiple(input_list):
    '''
    https://www.geeksforgeeks.org/stock-buy-sell/
    Here we can sell multiple times instead of just once.

    approach: Find local maxima and minima.
    :param input_list:
    :return: pair of buy,sell
    '''

    local_min= float('inf')
    answer=[]
    for idx in xrange(len(input_list)-1):
        curr_val= input_list[idx]
        local_min= min(local_min,curr_val)
        if curr_val >= input_list[idx+1]:
            answer.append((local_min, curr_val))
            local_min = input_list[idx+1]

        if idx == len(input_list)-1:
            answer.append((local_min, input_list[idx]))

    return answer



if __name__ == '__main__':
    stock_prices = [10, 7, 5, 8, 11, 9]
    print get_max_profit(stock_prices)
    print greedy_get_max_profit(stock_prices)

    print greedy_get_max_profit([6, 5, 4, 3, 2, 1])

    print get_max_profit_multiple([100, 180, 260, 310, 40, 535, 695])
