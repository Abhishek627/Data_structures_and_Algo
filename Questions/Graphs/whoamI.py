'''
https://www.hiredintech.com/classrooms/algorithm-design/lesson/34/task/21

Given is a matrix and a starting point and end point. Find smallest path containing all 0.
Another caveat is: Find the starting point first as it is given in form of a smaller matrix too.

Inputs in matrices: 0 -empty, 1-blocked, 2- starting point of the robot

Return -1 if no possible match from smaller matrix to bigger one, -2 if there is no path from atleast 1 pattern
(in case of multiple pattern matches)
'''

def find_start(input,matrix, pattern_matrix):
    pass

def who_am_i(input_matrix, pattern_matrix):
    start = find_start(input_matrix,pattern_matrix)
    if start==(-1,-1):
        return -1


if __name__ == '__main__':
    N,M,P,Q = map(int, raw_input().split(' '))
    X, Y = map(int, raw_input().split(' '))
    input_matrix= [list(raw_input()) for i in range(N)]
    pattern_matrix = [list(raw_input()) for k in range(P)]

    print input_matrix
    print pattern_matrix