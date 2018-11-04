'''
Pillai arithmetic function represents sum of gcd(num,i) from i=1 to num.
This can also be represented as sum (d* totient(num/d)) where d is a divisor

'''

from Euler_totient import euler_totient_m2
from math import sqrt
from fractions import gcd


def pillai_value_gcd(number):
    #method 1
    result =0
    for i in xrange(1,number+1):
        result += gcd(i,number)
    return result

def pillai_value_totient(number):
    result =0
    for i in xrange(1,int(sqrt(number))+1):
        if number %i ==0:
            result += i * euler_totient_m2(number/i)
            if i != number / i:
                result += (number / i) * euler_totient_m2(i)
    return result


if __name__ == '__main__':
    for i in xrange(1,20):
        print pillai_value_gcd(i) , pillai_value_totient(i)