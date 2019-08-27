'''
https://practice.geeksforgeeks.org/problems/activity-selection/0
given start and end tim eof activities. Find how many activities a single person can complete.
'''


def activity_num(timings):
    if not timings:
        return 0
    end_prev = timings[0][1]
    count = 1
    for item in timings[1:]:
        if item[0] >= end_prev:
            count += 1
            end_prev = item[1]
    return count

def N_meeting_rooms(timings):
    if not timings:
        return 0
    end_prev = timings[0][1]
    result =[timings[0][2]]
    for item in timings[1:]:
        if item[0] >= end_prev:
            result.append(item[2])
            end_prev = item[1]
    return result

if __name__ == '__main__':
    t = int(raw_input())
    for _ in xrange(t):
        n = int(raw_input())
        start_time = map(int, raw_input().split())
        end_time = map(int, raw_input().split())
        idx = [i for i in range(1,n+1)]
        timings = zip(start_time, end_time,idx)
        timings.sort(key=lambda x: x[1])
        print timings
        print "\n"
        # print activity_num(timings)
        # print "\n"

        print N_meeting_rooms(timings)
