'''
Given a matrix with each entry as cost of going throught that path. We have to find cost to travel from top left to bottom
right. Allowed directions are - left, right and diagonal.
'''


def min_cost_path(matrix, rows, cols, dp):
    dp[0][0] = matrix[0][0]

    for i in xrange(1, rows):
        dp[i][0] = dp[i - 1][0] + matrix[i][0]

    for i in xrange(1, cols):
        dp[0][i] = dp[0][i - 1] + matrix[0][i]

    for i in xrange(1, rows):
        for j in xrange(1, cols):
            dp[i][j] = matrix[i][j] + min(dp[i - 1][j], dp[i - 1][j - 1], dp[i][j - 1])
    return dp[-1][-1]


if __name__ == '__main__':
    matrix = [[1, 2, 3], [4, 8, 2], [1, 5, 3]]
    dp = [[0 for _ in range(len(matrix[0]))] for _ in range(len(matrix))]
    print min_cost_path(matrix, len(matrix), len(matrix[0]), dp)
