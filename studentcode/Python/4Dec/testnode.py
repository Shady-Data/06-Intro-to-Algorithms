# This file will test the node class

from node import Node

head = None

# Add five nodes to the beginning of the linked structure
for count in range(1,6):
    head = Node(count, head)

# print the contents of the structure
while head != None:
    print(head.data)
    head = head.next

'''
- One pointer, head, generates the linked structure. This pointer is manipulated
    in such a way that the most recently inserted item is always at the beginning
    of the structure
- When the data is displayed, they appear in the reverse order of their insertion
- Also, when the data is displayed, the head pointer is reset ti the next node, until
    the head pointer becomes None. Thus, at the end of this process, the nodes are
    effectively deleted from the linked structure. They are no longer available to
    the program and are recycled during the next garbage collection
'''