'''
https://leetcode.com/problems/longest-substring-without-repeating-characters/
'''


class Solution(object):
    def lengthOfLongestSubstring(self, s):
        """
        :type s: str
        :rtype: int
        """
        from collections import defaultdict
        hash_s = defaultdict(int)
        if len(s)<2:
            ans_len = len(s)
        else:
            ans_len=0
        start = end = 0
        while (end < len(s)):
            end_char = s[end]
            if end_char in hash_s and hash_s[end_char]>=start:
                start+=1
            else:
                hash_s[end_char] = end
                end += 1
            ans_len= max(end-start,ans_len)
        return ans_len



s="bbbbbb"
print Solution().lengthOfLongestSubstring(s)