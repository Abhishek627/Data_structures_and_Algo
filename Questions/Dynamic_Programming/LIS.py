'''
Longest increasing subsequence

If the list is [16, 3, 5, 19, 10, 14, 12, 0, 15] one possible answer is the subsequence [3, 5, 10, 12, 15],
another is [3, 5, 10, 14, 15].
If the list has only one integer, for example: [14], the correct answer is [14].
One more example: [10, 8, 6, 4, 2, 0], a possible correct answer is [8].

'''


def LIS_length(input_list):
    '''
    :param input_list:
    :return: size of LIS
    '''
    LIS_list = [1] * len(input_list)
    for i in xrange(len(input_list)):
        for j in xrange(0, i):
            if input_list[i] > input_list[j]:
                LIS_list[i] = max(LIS_list[i], LIS_list[j] + 1)
    return max(LIS_list)


def LIS_sol(input_list):
    '''
    prints possible LIS, O(N^2) solution
    :param input_list:
    :return:
    '''
    LIS = [[] for _ in xrange(len(input_list))]
    LIS[0].append(input_list[0])
    for i in xrange(1, len(input_list)):
        for j in xrange(0, i):
            if input_list[j] < input_list[i] and (len(LIS[i]) < len(LIS[j]) + 1):
                LIS[i] = LIS[j][:]
        LIS[i].append(input_list[i])

    answer = []
    max_len = 0
    for item in LIS:
        if len(item) > max_len:
            answer = item
            max_len = len(item)
    print answer


def LIS_binary_search(input_list):
    '''
    O(n*log(n)) solution:
    Basically, maintain 2 arrays, M and P
    table[i]  ----- store the index of smallest elem before index i , which forms a LIS with this elem as last elem
    preIndex[j] ------ store the index of previous elem in this LIS with input_list[j] as last elem

    table is guranteed to be a increasing input_list, therefore, we can use binary search here to find position of this elem
    :param input_list:
    :return:
    '''
    import bisect
    table = []
    tableIndex = []
    preIndex = []

    for i in range(len(input_list)):
        index = bisect.bisect_left(table, input_list[i])
        if index == len(table):
            table.append(input_list[i])
            tableIndex.append(i)
        else:
            table[index] = input_list[i]
            tableIndex[index] = i

        if index > 0:
            preIndex.append(tableIndex[index - 1])
        else:
            preIndex.append(-1)

    pos = tableIndex[-1]
    i = len(table) - 1
    while pos > -1:
        table[i] = input_list[pos]
        pos = preIndex[pos]
        i -= 1

    return table




if __name__ == '__main__':
    input_list = [16, 3, 5, 19, 10, 14, 12, 0, 15]
    print LIS_length(input_list),
    LIS_sol(input_list)

    input_list = [14]
    print LIS_length(input_list),
    LIS_sol(input_list)

    input_list = [10, 8, 6, 4, 2, 0]
    print LIS_length(input_list),
    LIS_sol(input_list)

    input_list = [3, 2, 6, 4, 5, 1]
    print LIS_length(input_list),
    LIS_sol(input_list)

    input_list = [4,2,3,12,11]
    print LIS_binary_search(input_list) ,  LIS_sol(input_list)