# This class will represent a singly linked node

class Node():
    def __init__(self, data, next = None):
        # Instantiates a Node with a default next of none
        self.data = data
        self.next = next

# The LinkedList class will instantiate Node objects and we'll add methods 
# to this class to add functionality
class LinkedList:
    def __init__(self):
        self.head = None

    # printing our linked list
    def print_linked_list(self):
        probe = self.head
        while probe != None:
            print(probe.data)
            probe = probe.next

    # add things to the end of the linked list
    def append(self, data):
        # Instantiate a new head
        newNode = Node(data)
        # is there something in our linked list yet ?
        if self.head is None:
            self.head = newNode
        # There are node(s) in our linked list
        else:
            probe = self.head
            # is probe at the end of the linked list?
            while probe.next != None:
                probe = probe.next
            probe.next = newNode

    # add node to beginning of the linked list
    def prepend(self, data):
        # Add a new node object containing the data to head with the current head as the next Node
        self.head = Node(data, self.head)

    # inserting node within the linked list
    def insert_node(self, index, data):
        # Is linked list empty or index less than 0
        if self.head is None or index <= 0:
            self.head = Node(data, self.head)
        # find our position to insert
        else:
            # Search for node at position index -1 or the last position
            probe = self.head
            while index > 1 and probe.next != None:
                probe = probe.next
                index -= 1
            # insert new node after node at position index -1 or last index
            probe.next = Node(data, probe.next)

    # remove a node by index
    def delete_node(self, index):
        # is this the only node
        if index <= 0 or self.head.next is None:
            removedItem = self.head.data
            self.head = self.head.next
        else:
            probe = self.head
            while index > 1 and probe.next.next != None:
                probe = probe.next
                index -= 1
            removedItem = probe.next.data
            probe.next = probe.next.next
        return removedItem

'''
Circular Linked List - Special case of a singly linked list
                        Insertion and removal of the first node are special cases of the insert ith
                        and remove ith operations on a singly linked list. These are special because
                        the head the head pointer must be reset. You can use circular linked list
                        with a dummy header node. Contains a link from the last node back to the first
                        node in the structure
'''

class CircularLinked:
    def __init__(self):
        self.head = None

    def print_linked_list(self):
        probe = self.head
        # misses last item
        while probe.next != self.head:
            print(probe.data)
            probe = probe.next
        # print the last item
        print(probe.data)


    def append(self, data):
        if not self.head:
            self.head = Node(data)
            self.head.next = self.head
        else:
            # newNode = Node(data, self.head)
            probe = self.head
            while probe.next != self.head:
                probe = probe.next
            # probe.next = newNode
            probe.next = Node(data, self.head)