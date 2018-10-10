'''
Sample Linked list code in python 2.7
__author__: Abhishek Sharma
'''


class Element(object):
    def __init__(self, data):
        self.data = data
        self.next = None


class LinkedList(object):
    def __init__(self, element=None):
        self.head = element

    def append(self, new_elem):
        curr = self.head
        if self.head:
            while curr.next:
                curr = curr.next
            curr.next = new_elem
        else:
            self.head = new_elem

    def print_ll(self):
        entry = []
        curr = self.head
        while curr:
            entry.append(curr.data)
            curr = curr.next
        for i in entry[:len(entry) - 1]:
            print str(i) + ' -->',
        print str(entry[-1])

    def get_position(self, position):
        if position < 1:
            return None
        curr = self.head
        for i in xrange(1, position):
            if curr:
                curr = curr.next
            else:
                break
        return curr.data if curr else None

    def insert(self, new_elem, position):
        counter = 1
        curr = self.head
        if position == 1:
            new_elem.next = curr
            self.head = new_elem
        else:
            while curr and counter < position:
                if counter == position - 1:
                    new_elem.next = curr.next
                    curr.next = new_elem
                curr = curr.next
                counter += 1

    def delete(self, value):
        curr = self.head
        prev = None
        while curr.data != value and curr.next:
            prev = curr
            curr = curr.next
        if curr.data == value:
            if prev:
                prev.next = curr.next
            else:
                self.head = curr.next

if __name__ == '__main__':
    e1 = Element(10)
    e2 = Element(20)
    e3 = Element(30)

    ll = LinkedList(e1)
    ll.print_ll()
    ll.append(e2)
    ll.print_ll()
    ll.append(e3)
    ll.print_ll()

    print ll.get_position(1), ll.get_position(2), ll.get_position(3), ll.get_position(4), ll.get_position(-1)

    e4 = Element(100)
    ll.insert(e4, 2)
    ll.print_ll()
    ll.delete(20)
    ll.print_ll()
    ll.delete(10)
    ll.print_ll()
