'''
Given a list of integers. Generate the superset for that list
Eg: [1,2,3]
answer: [
  [3],
  [1],
  [2],
  [1,2,3],
  [1,3],
  [2,3],
  [1,2],
  []
]
'''


def superset_generation(input_list,start,curr_list,answer):
    answer.append(curr_list)
    for i in xrange(start,len(input_list)):
        superset_generation(input_list,i+1,curr_list+[input_list[i]],answer)


if __name__ == '__main__':
    input_list= [1,2,3]
    output=[]
    superset_generation(input_list,0,[],output)
    print output
