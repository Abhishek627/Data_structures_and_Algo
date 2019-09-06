'''
Given height of buildings, find the amount of water that can be trapped in b/w the buildings.
'''


def compute_water(heights):
    '''
    This is O(N) space and time.
    :param heights:
    :return:
    '''
    n = len(heights)
    if n < 3:
        return 0
    left_max = [0] * n
    right_max = [0] * n

    # Fill left and right array
    left_max[0] = heights[0]
    for idx in range(1, n):
        left_max[idx] = max(left_max[idx - 1], heights[idx])

    right_max[-1] = heights[-1]
    for idx in range(len(heights) - 2, -1, -1):
        right_max[idx] = max(right_max[idx + 1], heights[idx])

    result = 0
    for item in zip(left_max, right_max, heights):
        result += min(item[0], item[1]) - item[2]
    return result


def compute_water_optimized(heights):
    # We can save O(N) space by simply keeping track of 2 variables left_max and right_max using
    # 2 pointer approach
    n = len(heights)
    if n < 3:
        return 0
    left, right = 0, n - 1
    left_max, right_max = heights[left], heights[right]
    result = 0
    while left < right:
        left_max, right_max = max(left_max, heights[left]), max(right_max, heights[right])
        if left_max <= right_max:
            result += left_max - heights[left]
            left += 1
        else:
            result += right_max - heights[right]
            right -= 1
    return result


if __name__ == '__main__':
    heights = [0, 1, 0, 2, 1, 0, 1, 3, 2, 1, 2, 1]
    print compute_water(heights)

    print compute_water_optimized(heights)
