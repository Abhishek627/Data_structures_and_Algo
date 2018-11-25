'''
https://leetcode.com/problems/permutation-in-string/
'''

from collections import Counter
import collections

class Solution(object):
    def checkInclusion(self, s1, s2):
        """
        :type s1: str
        :type s2: str
        :rtype: bool
        """
        if len(s1) > len(s2):
            return False
        s1_dict = Counter(s1)
        s2_dict = Counter(s2[:len(s1)])
        r = len(s1)
        while s1_dict != s2_dict and r < len(s2):
            left_char= s2[r - len(s1)]
            s2_dict[left_char] -= 1
            if s2_dict[left_char] == 0:
                del s2_dict[left_char]
            s2_dict[s2[r]] += 1
            r += 1
        if s1_dict == s2_dict:
            return True
        else:
            return False


    def checkInclusion2(self, s1, s2):
        """
        :type s1: str
        :type s2: str
        :rtype: bool
        """

        # clarification: find a continuous substring in s2 that is a permutation/anagram of s1

        # Sol.1, hash map, counters
        # linear time, O(m) space, where m is the number of distinct chars in s1.

        book = collections.defaultdict(int)
        for c in s1:
            book[c]+=1

        k = len(s1)
        i = 0
        mcount = k      ### the counter for mismatch characters
        while i<len(s2):
            if s2[i] in book:
                if book[s2[i]]>0:
                    mcount-=1
                book[s2[i]]-=1

            if i>k-1 and s2[i-k] in book:
                book[s2[i-k]]+=1
                if book[s2[i-k]]>0:
                    mcount+=1

            # print book, mcount
            if mcount==0:
                return True

            i+=1

        return False

    def checkInclusion3(self,s1,s2):
        # Sol.2: define a way to hash a combination of characters: ord(c)**2
        # no hash map, no counters
        # linear time, constant space

        k = len(s1)
        key = sum([ord(c) ** 2 for c in s1])
        test = sum([ord(c) ** 2 for c in s2[:k]])
        if key == test:
            return True

        for i in range(k, len(s2)):
            test += ord(s2[i]) ** 2
            test -= ord(s2[i - k]) ** 2
            if test == key:
                return True

        return False

s1 = "ab"
s2 = "eidbaooooab"
print Solution().checkInclusion(s1, s2)
