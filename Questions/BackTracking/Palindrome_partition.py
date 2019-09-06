'''

'''


class Solution(object):
    def partition(self, s):
        """
        :type s: str
        :rtype: List[List[str]]
        """
        result = []
        self.partition_helper(s, result, [], 0)
        return result

    def partition_helper(self, s, result, temp, start):
        if start == len(s):
            result.append(temp)
        for i in xrange(start, len(s)):
            if self.is_palindrome(s[start:i+1]):
                self.partition_helper(s, result, temp + [s[start:i+1]], i + 1)

    def is_palindrome(self, s):
        return s == s[::-1]


if __name__ == '__main__':
    s = Solution()
    print s.partition("aab")
