import heapq


def merge(input_list):
    heapq.heapify(input_list)
    count=0
    while len(input_list)>1:
        temp = heapq.heappop(input_list) + heapq.heappop(input_list)
        count+=temp
        heapq.heappush(input_list,temp)
    return count



print merge([8,12,6,4])


