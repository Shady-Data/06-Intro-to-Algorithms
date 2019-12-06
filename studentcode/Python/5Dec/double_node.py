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


    def prepend(self, data):
        # takes the data can sets self.head to be a new Double node with the new data and the next node to be itself
        # the tail node does not need to be modified unless tail.prev is equal to none or self.head
        # if head is None (empty or broken list)
        if self.head is None:
            # set head to a Node containing data with tail reference to be the next item (Look into self healing based on head and tail refences)
            self.head = DoubleNode(data, self.tail)
            self.tail.prev = self.head
        # if the tail is refenced to the current head or is none
        elif self.tail == self.head or self.tail is None:
            # initialize the new node with the data and next attribute pointing to the current head
            newNode = DoubleNode(data, self.head)
            # set the current head.prev attribute to the new node
            self.head.prev = newNode
            # Set tail.prev to the current head (Is this necessary?)
            self.tail = self.head
            # set head to the new Node
            self.head = newNode
        else:
            # otherwise set the current head.prev to reference teh new node and the self.head to be the newNode refencing the old node
            newNode = DoubleNode(data, self.head)
            self.head.prev = newNode
            self.head = newNode


    # 2 cases to consider index = 0 (prepend the data), index in the list and appends if tail is reached
    def insert_node(self, index, data):
        # the index is 0, or less than 0, or the linked list is empty
        if index <= 0 or self.head is None:
            self.prepend(data)
        # Initializes a pointer, moves to the index -1 location, or the end of the list
        else:
            newNode = DoubleNode(data)
            probe = self.head
            while index > 1 and probe.next.next != None:
                probe = probe.next
                index -= 1
            # Set the current object at probe to be the prev attribute for the new node
            newNode.prev = probe
            # Set the next reference of the current probe object to be the next attribute of the new node
            newNode.next = probe.next
            # set the probes next object prev attribute to be the newNode
            probe.next.prev = newNode
            # finally set the current probe's next attribute to be the new node
            probe.next = newNode

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
                        if probe.next.next is None:
                            # set the current probe's next attribute to be the next.next reference (effectively removes from the list)
                            probe.next = probe.next.next
                            self.tail = probe
                        else:
                            probe.next = probe.next.next
                            # set the new next node's previous attribute to be the probe
                            probe.next.prev = probe
                        probe = probe.next
                    else:
                        probe = probe.next
                    remove -= 1
                # if removedItem has not been changed
                if removedItem is False:
                    removedItem = probe.next.data
                    if probe.next.next is None:
                        # set the current probe's next attribute to be the next.next reference (effectively removes from the list)
                        probe.next = probe.next.next
                        self.tail = probe
                    else:
                        probe.next = probe.next.next
                        # set the new next node's previous attribute to be the probe
                        probe.next.prev = probe
            # otherwise remove is a value
            else:
                while probe.next.data != remove and probe.next.next != None:
                    probe = probe.next
                removedItem = probe.next.data
                if probe.next.next is None:
                    # set the current probe's next attribute to be the next.next reference (effectively removes from the list)
                    probe.next = probe.next.next
                    self.tail = probe
                else:
                    probe.next = probe.next.next
                    # set the new next node's previous attribute to be the probe
                    probe.next.prev = probe
        return removedItem

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
        probeFor = self.head
        probeRev = self.tail
        while probeFor != probeRev and probeRev != probeFor: # works for odd, need even break
            temp = probeFor.data
            probeFor.data = probeRev.data
            probeRev.data = temp
            probeFor = probeFor.next
            probeRev = probeRev.prev
            # if probeFor.prev is probeRev and probeRev.next is probeFor
            # then the linked list has an even number of nodes and all swaps have been completed
            if probeRev.next == probeFor and probeFor.prev == probeRev:
                break

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

    def __len__(self):
        count = 0
        probe = self.head
        while probe != None:
            probe = probe.next
            count += 1
        return count

'''
    def delete_node(self, index):
        # is this the only node
        if index <= 0 or self.head.next is self.tail:
            removedItem = self.head.data
            self.head = self.head.next
            self.head.prev = None
        else:
            probe = self.head
            while index > 1 and probe.next.next != None:
                probe = probe.next
                index -= 1
            # remove the next object
            removedItem = probe.next.data
            # if probe.next.next is None, we are at the end of the list and tail should point to the current probe
            if probe.next.next is None:
                # set the current probe's next attribute to be the next.next reference (effectively removes from the list)
                probe.next = probe.next.next
                self.tail = probe
            else:
                probe.next = probe.next.next
                # set the new next node's previous attribute to be the probe
                probe.next.prev = probe
        return removedItem
'''

doubly_linked_list = DoubleLinkedList()
doubly_linked_list.append("First node's data")
doubly_linked_list.append([1,2, "howdy"])
doubly_linked_list.append('test')
doubly_linked_list.prepend('A')
doubly_linked_list.prepend('B')
doubly_linked_list.insert_node(0, 'a')
doubly_linked_list.insert_node(3, 'x')
doubly_linked_list.insert_node(30, 'z')
doubly_linked_list.print_linked_list()
print()
print(doubly_linked_list.delete_node(0))
print(doubly_linked_list.delete_node(4))
print(doubly_linked_list.delete_node('A'))
print(doubly_linked_list.delete_node(20))
print()
doubly_linked_list.swap_node(0, 4)
doubly_linked_list.print_linked_list()
doubly_linked_list.reverse()
print()
doubly_linked_list.print_linked_list()
print()
doubly_linked_list.prepend('Odd')
doubly_linked_list.print_linked_list()
print()
doubly_linked_list.reverse()
doubly_linked_list.print_linked_list()
print()
doubly_linked_list.append('A')
print(doubly_linked_list.count_ocurrences('A'))

