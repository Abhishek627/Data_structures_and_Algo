'''
Given a list of integers. Generate the superset for that list
Eg: [1,2,3]
answer: [
  [3],
  [1],
  [2],
  [1,2,3],
  [1,3],
  [2,3],
  [1,2],
  []
]
'''


def superset_generation(input_list, start, curr_list, answer):
    answer.append(curr_list)
    for i in xrange(start, len(input_list)):
        superset_generation(input_list, i + 1, curr_list + [input_list[i]], answer)

def superset_generation_duplicate(input_list, start, curr_list, answer):
    answer.append(curr_list)
    for i in xrange(start, len(input_list)):
        if i>start and input_list[i]==input_list[i-1]:
            continue
        superset_generation_duplicate(input_list, i + 1, curr_list + [input_list[i]], answer)

def superset_bfs(input_list):
    result =[[]]
    for num in input_list:
        result += [r + [num] for r in result]
    return result


def superset_bit(input_list):
    # use bit manipulation to generate power set
    num_elm = len(input_list)
    power_set_len = 2 ** num_elm
    answer = [[] for _ in xrange(power_set_len)]
    for i in xrange(num_elm):
        for j in xrange(power_set_len):
            if (j >> i) & 1:
                answer[j].append(input_list[i])
    return answer

def superset_duplicate(nums):
    '''
    Add element only to recently added elements in last round, curr keeps track of that
    :param nums:
    :return:
    '''
    if not nums:
        return []
    nums.sort()
    res, cur = [[]], []
    for i in range(len(nums)):
        if i > 0 and nums[i] == nums[i - 1]:
            cur = [item + [nums[i]] for item in cur]
        else:
            cur = [item + [nums[i]] for item in res]
        res += cur
    return res

if __name__ == '__main__':
    input_list = [1, 2, 3]
    output = []
    superset_generation(input_list, 0, [], output)
    print output

    print superset_bit(input_list)

    print superset_bfs(input_list)

    duplicate_list= [1,2,2]
    print superset_duplicate(duplicate_list)

    output_dup=[]
    superset_generation_duplicate(duplicate_list, 0, [], output_dup)
    print output_dup
