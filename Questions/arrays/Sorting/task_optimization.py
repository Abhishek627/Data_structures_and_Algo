'''

https://www.hiredintech.com/classrooms/algorithm-design/lesson/19/task/17

'''


def maximum_completed_tasks(n, t, task_difficulties):
    # Write your code here
    task_difficulties.sort()
    if task_difficulties[0] > t:
        return 0

    task_rem = t- task_difficulties[0]
    count=1
    idx=1
    while idx < len(task_difficulties) :
        curr_task = task_difficulties[idx]
        task_rem = task_rem - curr_task - abs(curr_task-task_difficulties[idx-1])
        if task_rem >0:
            count+=1
        idx+=1

    return count


if __name__ == '__main__':
    print maximum_completed_tasks(5,65,[24,23,22,10,20])