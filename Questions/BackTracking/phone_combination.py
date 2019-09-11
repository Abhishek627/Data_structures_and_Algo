class Solution(object):
    def __init__(self):
        self.phone_dict = {"2": "abc", "3": "def", "4": "ghi", "5": "jkl", "6": "mno", "7": "pqrs", "8": "tuv",
                           "9": "wxyz"}

    def letterCombinations(self, digits):
        """
        :type digits: str
        :rtype: List[str]
        """

        result = []
        self.letterCombinationHelper(digits, result, 0, "")
        return result

    def letterCombinationHelper(self,digits, result, start, temp):
        if len(temp) == len(digits):
            result.append(temp)
            return

        for i in self.phone_dict[digits[start]]:
            self.letterCombinationHelper(digits, result, start + 1, temp + i)


if __name__ == '__main__':
    print Solution().letterCombinations("")