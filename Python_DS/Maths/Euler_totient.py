'''
https://www.geeksforgeeks.org/eulers-totient-function/
Euler totient function:
    totient(n)= total numbers less than n, which does not share a common factor with n (>1),or gcd(n,x)=1

    How to find totient value?
    a. Loop from 1 to n, and output values where gcd(num,value)==1 .

    b. It can also be desribed as , n * product of (1-1/x)   where x are the prime factors of n
        Example totient(6)= 6*(1-1/3)*(1-1/2)

'''
from math import sqrt


def gcd(a, b):
    if b == 0:
        return a
    else:
        return gcd(b, a % b)


def euler_totient_m1(number):
    # using method a
    result = 1
    for i in xrange(2, number):
        if gcd(number, i) == 1:
            result += 1
    return result


def euler_totient_m2(number):
    # using method b
    result = number
    for i in xrange(2, int(sqrt(number))+1):
        if (number % i == 0):
            while (number % i == 0):
                number /=  i
            result -= result / i
    if number > 1:
        result -= result / number
    return result


if __name__ == '__main__':
    for i in xrange(1, 11):
        print i, euler_totient_m1(i), euler_totient_m2(i)
