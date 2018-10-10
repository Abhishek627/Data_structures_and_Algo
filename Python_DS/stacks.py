'''
Basic implementation of stacks in python 2.7
Python supports stack functionality in inbuilt list.
https://docs.python.org/2/tutorial/datastructures.html#using-lists-as-stacks
__author__: Abhishek Sharma
'''

from Linked_list import Element, LinkedList


class Inbuilt_Stack(object):
    '''
    Array implementation of stacks
    '''

    def __init__(self):
        self.stack = []

    def push(self, val):
        self.stack.append(val)

    def pop(self):
        if len(self.stack) < 1:
            print "Stack Underflow error"
        else:
            print self.stack.pop()

    def top(self):
        if len(self.stack) < 1:
            print "Stack is empty"
        else:
            print self.stack[-1]

    def size(self):
        print len(self.stack)


class Stack_LinkedList(LinkedList):
    '''
    Linked List implementation of stack
    '''

    def push(self, new_elem):
        '''
        This should append new entry to the head
        We don't want to add to the end as that'll be O(n) (due to traversal of whole linked list )
        '''
        new_elem.next= self.head
        self.head =  new_elem

    def pop(self):
        '''
        This should print and delete first entry ,i.e, head.
        We don't want to remove from end as that'll be O(n) (due to traversal of whole linked list )
        '''
        deleted = self.head
        if self.head:
            self.head = self.head.next
            deleted.next = None
        print deleted.data


if __name__ == '__main__':
    #Array/List approach
    stack = Inbuilt_Stack()
    stack.push(1)
    stack.push(2)
    stack.push(3)
    stack.push(4)
    stack.push(5)
    stack.size()

    #LL approach
    ll= LinkedList()
    ll_stack= Stack_LinkedList(ll)
    ll_stack.push(Element(10))
    ll_stack.push(Element(20))
    ll_stack.push(Element(30))
    ll_stack.push(Element(40))


    ll_stack.pop()
    ll_stack.pop()







