from node import Node
head = None
targetItem = None
newItem = None
index = 0
'''
**************** Linked Structures ****************

A linked structure is a concrete data type that implements many types of collections, including lists.

As the name implies, a linked structure consists of items that are linked to other items.
The two that we'll go over are Singly Linked Structures and Doubly Linked Structures.

- Head Link - the first item of a linked structure
- Tail Link - an external link in a doubly linked structure to access the last item directly
- Empty Link - The absence of a link, indicated by the slash in the diagram

- The last item in either structure has no link to the next item

- Node - The basic unit of representation in a linked structure
    - comprised of two items
        - A Data Item
        - A Link to the next node in the structure

In python we set up nodes and linked structures by using references to objects

**************** Operations on Linked Structures ****************

- Arrays are already index based, because the indices are an integral part of the array structure
- We must emulate index-based operations on a linked structure by manipulating linkes within the structure.

- Traversal - Uses a temporary pointer variable named probe. This variable
                is initialized to the linked structure's head pointer and then controls
                a loop as follows.
'''

probe = head
while probe != None:
    # other code here
    probe = probe.next
'''

- Searching - The sequential search of a linked structure resembles a traversal
                in that you must start at the first node and follow links until
                you reach a sentinel
            - two possible sentinels, empty link(end of structure), or you find
                your item.
'''

probe = head
while probe != None and targetItem != probe.data:
    probe = probe.next
if probe != None:
    # if you find your item, some other code
    print('') # Added to clear error for no code under the if:
else:
    # target is not in list
    print('') # Added to clear error for no code under the else:

'''
- Accessing our ith item
    Similar to a sequential search, we can't go straight to i
    start at the first node and count the number of links until you reach the ith node
    Linked stuctures do not support random access
'''

# Assumes 0 <= index < n
probe = head
while index > 0:
    probe = probe.next
    index -= 1
# return probe.data

'''
Replacement - Also employs this kind of traversal pattern. You search for a given item
                or position and replace that item when found. If no item is found
                then no replacement happens and the operation returns False. If
                replacement occurs the operation returns True
'''

probe = head
while probe != None and targetItem != probe.data:
    probe = probe.next
if probe != None:
    probe.data = newItem
    # return True
else:
    # return False
    print('') # Added to clear error for no code under the else:

'''
Inserting at the Beginning - better than linear complexity operation on a linked structure

'''
head = Node(newItem, head)


'''
Inserting at the End - Consider two cases
                        The head pointer is None, so the head pointer is set to the new node
                        The head pointer is not None, so the code searches for the last
                        node and aims its next pointer at the new node.
'''

newNode = Node(newItem)
if head is None:
    head = newNode
else:
    probe = head
    while probe.next != None:
        probe = probe.next
    probe.next = newNode

'''
Removing at beginning - this operation returns the removed item
'''

# Assumes at least one node in the structure
removedItem = head.data
head = head.next
# return removedItem

'''
Removing at the End - Two cases to consider
                        There is just one node. The head pointer is set to None
                        There is a node before the last node. The code searches for the second-to-last
                        node and sets its next pointer to None
'''

# Assumes at least on node in structure
removedItem = head.data
if head.next is None:
    head = None
else:
    probe = head
    while probe.next.next != None:
        probe = probe.next
    removedItem = probe.next.data
    probe.next = None
# return removedItem

'''
Inserting at Any Position - Two cases to consider
                            The nodes next pointer is None. This means i >= n, so you should
                                place the new item at the end of the linked structure
                            The nodes next pointer is not None. That means that 0 < i < n, so you must
                                place the new item between the node at position i-1 and the node at i
'''
if head is None or index <= 0:
    head = Node(newItem, head)
else:
    probe = head
    while index > 1 and probe.next != None:
        probe = probe.next
        index -= 1
    # Insert new node after node at position index -1 of last position
    probe.next = Node(newItem, probe.next)

'''
Removing at Any Position - Consider three cases
                            i <= 0 - you use the code to remove the first item
                            0 < i < n - You search for the node at position i-1, as in insertion and remove the following node
                            i >= n - You remove the last node
'''

# Assumes the the linked structure has at least one item
if index <= 0 or head.next is None:
    removedItem = head.data
    head = head.next
    # return removedItem
else:
    # Search for node at position index - 1 or next to last position
    probe = head
    while index > 1 and probe.next.next != None:
        probe = probe.next
        index -= 1
    removedItem = probe.next.data
    probe.next = probe.next.next
    # return removedItem