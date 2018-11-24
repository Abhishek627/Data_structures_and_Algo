'''
Problems is given 2 strings S,T. Find the min window in S which contains all the characters in T.

solution strategy:
1. O(N^2): start with win size len(unique_char_in_T) and increase till I get a match
2. Sliding window

'''

from collections import Counter


def minWindow(S, T):
    T_dict = Counter(T)
    found = len(T_dict)
    ans_size = float("inf")
    start = end = 0
    answer=""

    while (end < len(S)):
        if S[end] in T_dict:
            T_dict[S[end]]-=1
            if T_dict[S[end]]==0 : found-=1
        end+=1
        while (found == 0):
            # Increment left pointer and check if another optimal answer exists
            if end-start < ans_size:
                ans_size = end-start
                answer= S[start:end]

            start_elem = S[start]
            if start_elem in T_dict:
                T_dict[start_elem]+=1
                if T_dict[start_elem]>0:
                    found+=1
            start+=1
    return answer



if __name__ == '__main__':
    S = "ADOBECODEBANC"
    T = "ABC"
    result = minWindow(S, T)
    print result
    assert (result == 'BANC')
