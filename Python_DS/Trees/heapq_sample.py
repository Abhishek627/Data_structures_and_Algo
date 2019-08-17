'''
Trying out python's inbuilt heap library

'''
import heapq


def create_heap(input_list):
    heapq.heapify(input_list)


def get_min_elem(heap):
    return heapq.heappop(heap)


def insert_elem(heap, new_item):
    return heapq.heappush(heap, new_item)


if __name__ == '__main__':
    # create a min heap
    a = [11, 2, 3, 4, 5, 6, 7, 8, 9, 10]
    create_heap(a)

    # should return 2
    print get_min_elem(a)

    insert_elem(a, 1)
    # should return 1
    print  a[0]
    print a

    print heapq.nlargest(3, a), heapq.nsmallest(3, a)

    # create max heap
    a = [11, 2, 3, 4, 5, 6, 7, 8, 9, 10]
    # a = [-1 * i for i in a]
    create_heap(a)
    # print "Maximum elem is ", -1 * get_min_elem(a)
    print heapq.nlargest(3, a), heapq.nsmallest(3, a)
