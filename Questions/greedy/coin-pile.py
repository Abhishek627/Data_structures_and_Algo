'''
https://practice.geeksforgeeks.org/problems/coin-piles/0
'''


def coin_pile(coins,k):
    result= 0
    prev = coins[0]
    for idx,val in enumerate(coins[1:]):
        if abs(val-prev) >= k:
            temp= val-prev-k
            coins[idx]= val- temp
            result+=temp
    return result


if __name__ == '__main__':
    t = int(raw_input())
    for _ in range(t):
        n,k = map(int, raw_input().split())
        coins = map(int, raw_input().split())
        print coin_pile(coins,k)