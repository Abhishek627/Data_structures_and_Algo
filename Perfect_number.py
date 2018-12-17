class Solution:
    # @param A : integer
    # @return a strings

    def solve(self, A):
        count = 0
        for i in xrange(1,10**12):
            num = str(i)
            if len(num) % 2 == 0 and self.is_one_two(num) and self.is_palindrome(num):
                count += 1
                if count == A:
                    return num

    def is_one_two(self, num):
        string_set = {'1', '2'}
        num_set = set(num)
        return string_set == num_set or num_set == {'1'} or num_set == {'2'}

    def is_palindrome(self, num):
        return num == num[::-1]



if __name__ == '__main__':
    print Solution().solve(40)