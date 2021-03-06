'''
https://www.hiredintech.com/classrooms/algorithm-design/lesson/76/task/26

input: 3 4 1 2 5 6 9 0 1 2 3 1
output: 4

'''


def jump_count(input_list):
    count=idx=0
    while idx< len(input_list):
        temp= input_list[idx]
        if temp>0:
            idx+= temp
            count+=1
        else:
            return -1
    return count


def is_numeric_palindrome(n):
    # Write your code here

    input_list= map(int,str(n))
    return input_list == input_list[::-1]


if __name__ == '__main__':
    input_list= [3, 4 ,1 ,2, 5, 6, 9, 0, 1 ,2, 3, 1]
    print jump_count(input_list)


    print is_numeric_palindrome(12001)