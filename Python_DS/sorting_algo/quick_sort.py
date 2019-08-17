'''
Pure python 2.7 implementation of quick sort.
Algo--
Step1: Select a good randomized pivot elem.
      [ We can simply select the rightmost/leftmost elem too but that'll mess up our worst case scenario]
Step2: Divide array/collection in 2 part,s.t, elem left of pivot are less than pivot and
       elem to the right of it are greater than it.
Step3: Follow step 1 and step 2 for left and right sub-arrays of pivot now
Easy-Peasy
'''

import random


def partition(input_array,start,end):
    random_pivot_idx = random.randint(start,end)
    input_array[random_pivot_idx],input_array[end]=input_array[end],input_array[random_pivot_idx]
    pivot= input_array[end]
    pindex=start
    for i in range(start,end):
        if(input_array[i]<= pivot):
            if (pindex!=i):
                input_array[i],input_array[pindex]= input_array[pindex],input_array[i]
            pindex+=1
    input_array[end], input_array[pindex]= input_array[pindex], input_array[end]
    return pindex

def quick_sort_recursive(input_array,start=0,end=None):
    end= len(input_array)-1 if end is None else end
    if start<end:
        pindex = partition(input_array,start,end)
        quick_sort_recursive(input_array,start,pindex-1)
        quick_sort_recursive(input_array,pindex+1,end)
    return

if __name__ == '__main__':
    print "With duplicates"
    for _ in xrange(5):
        input_array = [random.randrange(1, 20) for _ in xrange(10)]
        print "Before",input_array
        quick_sort_recursive(input_array)
        print "After",input_array
        print "\n"


    print "\n\nWithout duplicates"
    for _ in xrange(5):
        input_array = random.sample(range(10), 10)
        print "Before", input_array
        quick_sort_recursive(input_array)
        print "After", input_array
        print "\n"
