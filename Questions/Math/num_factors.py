'''
https://www.hiredintech.com/classrooms/algorithm-design/lesson/23/task/22

Count the number of factors of a number.
For example, 12 has 6 factors. (1,2,3,4,6,12)

solution is simple but the main issue is range of input is (1,10^12)
'''

import math

def count_numbers_factors(n):
    factor_list =[]
    last = int(math.sqrt(n))
    for i in range(1,last+1):
        if n%i == 0:
            factor_list.append(i)
            if last != n/last:
                factor_list.append(n/i)
    # print factor_list
    return len(factor_list)

def sum_the_divisiors(n):
    factor_list =[]
    last = int(math.sqrt(n))
    for i in range(1,last+1):
        if n%i == 0:
            factor_list.append(i)
            if last != n/last:
                factor_list.append(n/i)

    return sum(factor_list)



if __name__ == '__main__':
    print count_numbers_factors(144)
    print sum_the_divisiors(8)
    print sum_the_divisiors(7)
    print sum_the_divisiors(1)
    print sum_the_divisiors(1000)


