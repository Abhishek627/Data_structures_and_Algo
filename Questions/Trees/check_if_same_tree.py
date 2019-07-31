class Solution:
    # @param A : list of integers
    # @param B : list of integers
    # @param C : list of integers
    # @return an integer
    def solve(self, A, B, C):
        if (len(A) == len(B) and len(B) == len(C)):
            return  self.solve_helper(A, B, C, len(A))
        return 0


    def solve_helper(self, A, B, C, length):
        if length == 0 or len(A)==0:
            return 1

        if length == 1:
            return A[0] == B[0] and B[0] == C[0]

        idx = -1

        for i in range(len(B)):
            if len(A)>0 and A[0] == B[i]:
                idx = i
                break

        if idx == -1:
            return 0

        check_left = self.solve_helper(A[1:], B[:idx], C, length)
        check_right = self.solve_helper(A[idx + 1:], B[idx + 1:], C[idx:], length - idx - 1)

        return check_left and check_right


if __name__ == '__main__':
    A= [56, 80, 18, 37, 68, 7, 47, 27, 70, 59]
    B= [70, 37, 27, 47, 68, 56, 7, 18, 80, 59]
    C= [27, 68, 47, 70, 7, 80, 59, 18, 56, 37]
    print Solution().solve(A,B,C)