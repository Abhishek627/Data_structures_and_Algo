'''
https://www.hackerrank.com/challenges/minimum-swaps-2/problem?h_l=interview&playlist_slugs%5B%5D=interview-preparation-kit&playlist_slugs%5B%5D=arrays
'''

# Function returns the minimum
# number of swaps required to sort the array

def minSwaps(arr):
    n = len(arr)

    arrpos = list(enumerate(arr))

    arrpos.sort(key=lambda it: it[1])

    vis = {k: False for k in range(n)}

    ans = 0
    for i in range(n):
        if vis[i] or arrpos[i][0] == i:
            continue

        cycle_size = 0
        while not vis[i]:
            vis[i] = True
            i = arrpos[i][0]
            cycle_size += 1

        if cycle_size > 0:
            ans += (cycle_size - 1)
    return ans


arr = [1, 5, 4, 3, 2]
print(minSwaps(arr))
