'''
Question is to find all the prime factors of a number.
https://www.hiredintech.com/classrooms/algorithm-design/lesson/23/task/30/solution

Solution:
1. Iterate from 2 to sqrt(num) and check if the num is divisble by ith elem and if ith elem is a prime number
!!!!! But we don't need to check ith elem for primality as if it wasn't a prime ,
 we would have encountered one of it's factor earlier than ith elem too
'''


def all_prime_factors(n):
    # Write your code here
    # Return a list with the prime decomposition numbers
    import math
    result = []
    limit = int(math.sqrt(n))
    for i in range(2, limit):
        while n % i == 0:
            result.append(i)
            n /= i
    if n != 1:
        result.append(n)
    return result


if __name__ == '__main__':
    assert all_prime_factors(1105) == [5, 13, 17]
    assert all_prime_factors(64) == [2, 2, 2, 2, 2, 2]
    assert all_prime_factors(20) == [2, 2, 5]
    assert all_prime_factors(9901) == [9901]
