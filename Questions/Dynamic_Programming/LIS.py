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
    LIS_list=[1]* len(input_list)
    for i in xrange(len(input_list)):
        for j in xrange(0,i):
            if input_list[i]> input_list[j]:
                LIS_list[i] = max(LIS_list[i], LIS_list[j]+1)
    return max(LIS_list)

def LIS_sol(input_list):
    '''
    prints possible LIS
    :param input_list:
    :return:
    '''
    LIS = [ [] for _ in xrange(len(input_list))]
    LIS[0].append(input_list[0])
    for i in xrange(1,len(input_list)):
        for j in xrange(0,i):
            if input_list[j] < input_list[i] and (len(LIS[i]) < len(LIS[j])+1):
                LIS[i]= LIS[j][:]
        LIS[i].append(input_list[i])

    answer=[]
    max_len=0
    for item in LIS:
        if len(item)>max_len:
            answer=item
            max_len= len(item)
    print answer




if __name__ == '__main__':
    input_list= [16, 3, 5, 19, 10, 14, 12, 0, 15]
    print LIS_length(input_list),
    LIS_sol(input_list)


    input_list= [14]
    print LIS_length(input_list),
    LIS_sol(input_list)

    input_list= [10,8,6,4,2,0]
    print LIS_length(input_list),
    LIS_sol(input_list)

    input_list=[3,2,6,4,5,1]
    print LIS_length(input_list),
    LIS_sol(input_list)