'''
https://practice.geeksforgeeks.org/problems/page-faults-in-lru/0
Question wants us to find number of page faults in a LRU cache.
Solution will be creating a queue of size= capacity of muy cache. Create a hashmap to look whether incoming value is
there or not.
'''

from collections import deque


def page_faults(list, capacity):
    q = deque()
    exists = set()
    faults = 0
    for item in list:
        if item not in exists:
            if len(q) < capacity:
                q.append(item)
                exists.add(item)
            else:
                temp=q.popleft()
                exists.remove(temp)
                q.append(item)
                exists.add(item)
            faults+=1
        else:
            # handle hit case
            q.remove(item)
            q.append(item)

    return faults


if __name__ == '__main__':
    t = int(raw_input())
    for _ in range(t):
        n = int(raw_input())
        val = map(int, raw_input().split())
        capacity = int(raw_input())
        print page_faults(val, capacity)
