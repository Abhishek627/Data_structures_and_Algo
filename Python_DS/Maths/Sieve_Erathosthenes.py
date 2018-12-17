'''
Program to print prime numbers upto N.
Approach is to see if a number is prime or not, and mark multiple of it as not prime.
Then, simply traverse the marked array and print the values.

Time: O(n*log(log N))
Space: O(N)
'''


import math


def sieve_of_erathosthenes(N):
    prime_list = [1 for i in xrange(1, N + 1)]
    prime_list[0] = 0
    prime_list[1] = 0

    res_list = []
    for i in xrange(2, int(math.sqrt(N)) + 1):
        if prime_list[i]:
            j = i
            while i * j < N:
                prime_list[i * j] = 0
                j += 1

    for idx in xrange(len(prime_list)):
        if prime_list[idx] == 1:
            res_list.append(idx)

    return res_list


def sieve_erathosthenes_updated(N):
    # This one has time complexity of O(N) instead of normal O(N*log(log(N))
    #ToDo: Implement this
    pass


def segmented_sieve(N):
    # For cases when N is too large to keep in memory as a list.
    # Also useful if we have to find primes in a range

    limit = int(math.sqrt(N)) + 1
    prime_list = sieve_of_erathosthenes(limit)
    print prime_list

    low = limit
    high = 2 * limit

    while (low < N):
        high = min(high, N)

        temp_array = [True] * (limit + 1)
        for num in prime_list:
            # Mark entries in current ones as prime or not
            start_point = int(math.floor(low / num)) * num

            if start_point < low:
                start_point += num

            j = start_point
            while j < high:
                temp_array[j - low] = False
                j += num

        for entry in xrange(low, high):
            if temp_array[entry - low]:
                print entry,

        low += limit
        high += limit


if __name__ == '__main__':
    print sieve_of_erathosthenes(100)

    segmented_sieve(100)
