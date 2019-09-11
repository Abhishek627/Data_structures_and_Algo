class Solution(object):
    def distanceBetweenBusStops(self, distance, start, destination):
        """
        :type distance: List[int]
        :type start: int
        :type destination: int
        :rtype: int
        """
        if start > destination:
            start, destination = destination, start

        result = 0
        for val in distance:
            result += val

        temp = 0
        for idx in range(start, destination):
            temp += distance[idx]

        result = min(temp, result - temp)
        return result


class Solution2(object):
    def maximumSum(self, arr):
        """
        :type arr: List[int]
        :rtype: int
        """

        sum_now = arr[0]
        max_now = arr[0]
        for val in arr[1:]:
            sum_now = max(val, sum_now + val)
            max_now = max(sum_now, max_now)
        return max_now


if __name__ == '__main__':
    distance = [1, 2, 3, 4]
    start = 0
    destination = 3
    # print Solution().distanceBetweenBusStops(distance, start, destination)

    print Solution2().maximumSum([1, -2, 0, 3])
