'''
https://www.hiredintech.com/classrooms/algorithm-design/lesson/19/task/16
'''



def sort_the_files(n, result):
    i = 1
    while i <= min(n, 9):
        gen_filename(i, n, result)
        i += 1

    return

def gen_filename(d, p, result):
    if d > p:
        return
    if len(result) > 1000:
        return

    result.append('IMG'+str(d)+'.jpg')
    d *= 10
    for i in range(0, 10):
        gen_filename(d + i, p, result)



if __name__ == '__main__':
    result = []
    sort_the_files(16, result=result)
    print result
