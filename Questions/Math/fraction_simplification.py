'''
https://www.hiredintech.com/classrooms/algorithm-design/lesson/23/task/20

'''

def gcd(a,b):
    if b==0:
        return a
    return gcd(b,a%b)

def simplify_fraction(numerator, denominator, result):
    gcd_of_nums= gcd(numerator,denominator)
    if gcd_of_nums == 1:
        result.append(numerator)
        result.append(denominator)
    else:
        result.append(numerator/gcd_of_nums)
        result.append(denominator/gcd_of_nums)

if __name__ == '__main__':
    result=[]
    simplify_fraction(77,22,result)
    print result