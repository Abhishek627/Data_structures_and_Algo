'''
https://practice.geeksforgeeks.org/problems/largest-number-possible/0

Print the largest number that is possible from 'N' digits and sum 'S'
'''


def largest_number(N,S):
    result= 0
    for i in range(N-1,-1,-1):
        if S >= 9:
            S-=9
            result+= 9 * 10**i
        else:
            result+= S*10**i
            S=0
    result= str(result)
    if S > 0 or (N>0 and len(result)<N):
        return -1
    return result



if __name__ == '__main__':
    t = int(raw_input())
    for _ in range(t):
        N,S = map(int,raw_input().split())
        print largest_number(N,S)