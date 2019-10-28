'''
https://www.spoj.com/problems/COINS/
'''


def maxCoins(n):
    if n < 4:
        return n
    if n in result:
        return result[n]
    result[n] = max(n, maxCoins(n/2) + maxCoins(n/3) + maxCoins(n/4))
    return result[n]

while True:
    try:
        num = int(raw_input())
        result = {}
        print maxCoins(num)
    except EOFError:
        break