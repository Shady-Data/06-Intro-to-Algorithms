# Doubly Linked Lists - Very similar to singly linked, however these have a pointer and a tail node
#                       Move, left to previous node, from a given node
#                       Move immediately to the last node

class DoubleNode:
    def __init__(self, data, next = None, prev = None):
        self.data = data
        self.next = next
        self.prev = prev


class DoubleLinkedList:
    def __init__(self):
        self.head = None
        self.tail = None

    # two cases to consider
    def print_linked_list(self):
        probe = self.head
        while probe != None:
            print(probe.data)
            probe = probe.next

    def append(self, data):
        # empty linked list?
        if self.head is None:
            # newNode.prev = None
            # self.head = newNode
            self.head = DoubleNode(data, self.tail)
            self.tail = self.head
        # we have items in our list
        else:
            # instantiate a new node with the data and the current tail as the prev attribute
            newNode = DoubleNode(data, None, self.tail)
            # set the current tail's next attribute to be the new node
            self.tail.next = newNode
            # set the tail reference to the new final node (newNode)
            self.tail = newNode