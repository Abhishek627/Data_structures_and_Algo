'''
https://www.hiredintech.com/classrooms/algorithm-design/lesson/19/task/31
'''


def cover_the_border(l, radars):
    # Example arguments:
    # l = 100
    # radars = [ [5, 10], [3, 25], [46, 99], [39, 40], [45, 50] ]
    '''
    This is brute force solution which would fail for large values of l or if all the ranges are too big,
    it'll iterate over the strip again and again
    :param l:
    :param radars:
    :return:
    '''

    strip=[0]*l
    for entry in radars:
        start=entry[0]
        end= entry[1]
        for i in xrange(start,end):
            strip[i]=1

    return strip.count(1)


def cover_the_border_better(l, radars):
  # Example arguments:
  # l = 100
  # radars = [ [5, 10], [3, 25], [46, 99], [39, 40], [45, 50] ]
    endpoints = []
    for entry in radars:
      endpoints.append(['start',entry[0]])
      endpoints.append(['end',entry[1]])

    endpoints.sort(key=lambda k:k[1])
    last_open= -1
    open_ranges=0
    result=0
    for entry in endpoints:
        if entry[0]=='start':
            open_ranges+=1
            if open_ranges==1:
                last_open=entry[1]
        else:
            open_ranges-=1
            if open_ranges==0:
                result+= entry[1]-last_open
    return result



if __name__ == '__main__':
    # print cover_the_border(100,[ [5, 10], [3, 25], [46, 99], [39, 40], [45, 50] ])

    print cover_the_border_better(100,[ [5, 10], [3, 25], [46, 99], [39, 40], [45, 50] ])