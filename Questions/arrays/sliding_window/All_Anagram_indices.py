'''
https://leetcode.com/problems/find-all-anagrams-in-a-string/

Solution: Similar to min window question, just have to keep track of counter instead of minimum one
'''

from collections import defaultdict


def AnagramIndices(S, T):
    T_dict = defaultdict(int)
    for char in T:
        T_dict[char] += 1
    found = len(T_dict)
    start = end = 0
    answer = []

    while (end < len(S)):
        if S[end] in T_dict:
            T_dict[S[end]] -= 1
            if T_dict[S[end]] == 0: found -= 1
        end += 1
        while (found == 0):
            if end - start == len(T):
                answer.append(start)
            start_elem = S[start]
            if start_elem in T_dict:
                T_dict[start_elem] += 1
                if T_dict[start_elem] > 0:
                    found += 1
            start += 1
    return answer


if __name__ == '__main__':
    S = "cbaebabacd"
    T = "abc"
    result = AnagramIndices(S, T)
    print result

    s = "abab"
    p = "ab"
    print AnagramIndices(s, p)
