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


    # remove a node by index or value, default will be a value removal
    def delete_node(self, remove):
        # is this the only node
        if self.head.next is None or isinstance(remove, int) and remove <= 0:
            removedItem = self.head.data
            self.head = self.head.next
        else:
            # sentinel value to check if changed
            removedItem = False
            probe = self.head
            # determine if remove is an index or a value
            if isinstance(remove, int) and remove < self.__len__():
                # possible index value detected
                while remove > 1 and probe.next.next != None:
                    # if the probe.next.data is == remove
                    if probe.next.data == remove:
                        removedItem = probe.next.data
                        probe.next = probe.next.next
                        probe = probe.next
                    else:
                        probe = probe.next
                    remove -= 1
                # if removedItem has not been changed
                if removedItem is False:
                    removedItem = probe.next.data
                    probe.next = probe.next.next
            # otherwise remove is a value
            else:
                while probe.next.data != remove and probe.next.next != None:
                    probe = probe.next
                removedItem = probe.next.data
                probe.next = probe.next.next
        return removedItem

    # replace a node's value at index
    def replace_node(self, index, data):
        # Is linked list empty or index less than 0
        if self.head is None or index <= 0:
            self.head.data = data
        # find our position to insert
        else:
            # Search for node at position index or the last position
            probe = self.head
            while index > 0 and probe.next != None:
                probe = probe.next
                index -= 1
            # insert new node after node at position index or last index
            probe.data = data

    # the __len__() function allows the use of len() function
    def __len__(self):
        count = 0
        probe = self.head
        while probe != None:
            count += 1
            probe = probe.next
        return count

    def swap_node(self, index1, index2):
        # swaps the data of index 1 and 2, does nothing if the list is too short,
        # or both values are the same. If the index exceeds the number of items in the list
        # It uses the last viable node for that index
        # only if there are 2 or more entries in the list
        if self.head != None and self.head.next != None:
            if index1 <= 0:
                probe1 = self.head
            else:
                probe1 = self.head
                while index1 > 1 and probe1.next != None:
                    probe1 = probe1.next
                    index1 -= 1
            if index2 <= 0:
                probe2 = self.head
            else:
                probe2 = self.head
                while index2 > 1 and probe2.next != None:
                    probe2 = probe2.next
                    index2 -= 1
            # do nothing if the data values are the same
            if probe1.data != probe2.data:
                temp = probe1.data
                probe1.data = probe2.data
                probe2.data = temp
        
    def reverse(self):
        # mutate the linked list so that the values are reversed within the list
        values = []
        probe = self.head
        while probe != None:
            values.append(probe.data)
            probe = probe.next
        probe = self.head
        index = len(values) - 1
        while probe != None:
            probe.data = values[index]
            probe = probe.next
            index -= 1

    def count_ocurrences(self, value):
        # initialize a count accumalator
        count = 0
        # Traverse through the linked list checking if each node's data is equal to the value parameter
        probe = self.head
        while probe != None:
            if probe.data == value:
                count += 1
            probe = probe.next
        # return the count variable
        return count

# End of LinkedList Class

linked_list = LinkedList()
linked_list.append('A')
linked_list.append('Hello, I\'m the second node')
linked_list.prepend('I should be the beginning')
linked_list.prepend('Now I\'m first')
linked_list.insert_node(2, 'inserted')
linked_list.insert_node(24, 'next insert')
# linked_list.delete_node(1)
# linked_list.pop_node('A')
print(linked_list.delete_node('A'))
print(linked_list.delete_node(1))

# print(linked_list.head.data)

print('\tBefore Reverse:')
linked_list.print_linked_list()
print(len(linked_list))
linked_list.reverse()
print('\tAfter Reverse:')
linked_list.print_linked_list()

print(linked_list.count_ocurrences('inserted'))
print(linked_list.count_ocurrences('I should be the beginning'))

'''
    # remove a node by index
    def delete_node(self, index):
        # is this the only node
        if index <= 0 or self.head.next is None:
            removedItem = self.head.data
            self.head = self.head.next
        else:
            # remove a node by index
            probe = self.head
            while index > 1 and probe.next.next != None:
                probe = probe.next
                index -= 1
            removedItem = probe.next.data
            probe.next = probe.next.next
        return removedItem
'''
'''
    # remove a node by value
    def pop_node(self, value):
        # is this the only node
        if self.head.next is None or self.head.data == value:
            removedItem = self.head.data
            self.head = self.head.next
        else:
            probe = self.head
            while probe.next.data != value and probe.next.next != None:
                probe = probe.next
            removedItem = probe.next.data
            probe.next = probe.next.next
        return removedItem
'''




# Just and empty link
# node1 = None

# # A node containing data and an empty link
# node2 = Node('A', None)
# node3 = Node('B', node2)

# print(node3.data)

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

    def prepend(self, data):
        # Add a new node object containing the data to head with the current head as the next Node
        probe = self.head
        while probe.next != self.head:
            probe = probe.next
        self.head = Node(data, self.head)
        probe.next = self.head

    # inserting node within the linked list
    def insert_node(self, index, data):
        # Is linked list empty or index less than 0
        if self.head is None or index <= 0:
            self.head = Node(data, self.head)
        # find our position to insert
        else:
            # Search for node at position index -1 or the last position
            probe = self.head
            while index > 1 and probe.next != self.head:
                probe = probe.next
                index -= 1
            # insert new node after node at position index -1 or last index
            probe.next = Node(data, probe.next)

    # remove a node by index or value, default will be a value removal
    def delete_node(self, remove):
        # is this the only node
        if self.head.next is None or isinstance(remove, int) and remove <= 0:
            removedItem = self.head.data
            self.head = self.head.next
        else:
            # sentinel value to check if changed
            removedItem = False
            probe = self.head
            # determine if remove is an index or a value
            if isinstance(remove, int) and remove < self.__len__():
                # possible index value detected
                while remove > 1 and probe.next.next != self.head:
                    # if the probe.next.data is == remove
                    if probe.next.data == remove:
                        removedItem = probe.next.data
                        probe.next = probe.next.next
                        probe = probe.next
                    else:
                        probe = probe.next
                    remove -= 1
                # if removedItem has not been changed
                if removedItem is False:
                    removedItem = probe.next.data
                    probe.next = probe.next.next
            # otherwise remove is a value
            else:
                while probe.next.data != remove and probe.next.next != self.head:
                    probe = probe.next
                removedItem = probe.next.data
                probe.next = probe.next.next
        return removedItem

    def count_ocurrences(self, value):
        # initialize a count accumalator
        count = 0
        # Traverse through the linked list checking if each node's data is equal to the value parameter
        probe = self.head
        while probe.next != self.head:
            if probe.data == value:
                count += 1
            probe = probe.next
        # return the count variable
        return count


    def __len__(self):
        count = 0
        probe = self.head
        while probe.next != self.head:
            count += 1
            probe = probe.next
        return count

'''
    # remove a node by index
    def delete_node(self, index):
        # is this the only node
        if index <= 0 or self.head.next is self.head:
            removedItem = self.head.data
            self.head = None
        else:
            probe = self.head
            while index > 1 and probe.next.next != self.head:
                probe = probe.next
                index -= 1
            removedItem = probe.next.data
            probe.next = probe.next.next
        return removedItem
'''

# circular_linked_list = CircularLinked()
# circular_linked_list.append('A')
# circular_linked_list.append('B')
# circular_linked_list.append('C')
# circular_linked_list.prepend('1')
# circular_linked_list.prepend('2')
# circular_linked_list.prepend('3')
# circular_linked_list.insert_node(3, "inserted")
# print('Removed Node 2:', circular_linked_list.delete_node(2))
# print()
# circular_linked_list.print_linked_list()
