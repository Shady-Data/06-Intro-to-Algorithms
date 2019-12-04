from node import Node
"""
1. Using box and pointer notation, draw a picture of the nodes created by the 
first loop in the tester program. 
​"""

"""
2. What happens when a programmer attempts to access a node’s data fields when 
the node variable refers to None? How do you guard against it?
​"""
# node = None
# print(node.data)
# Traceback (most recent call last):
#   File "C:\Users\student\Documents\Curriculum\06-Intro-to-Algorithms\studentcode\Python\4Dec\basic_linked_questions.py", line 12, in <module>
#     print(node.data)
# AttributeError: 'NoneType' object has no attribute 'data'

# access the data with a while checkin if the node value equates to True (i.e. is not None, False, '', 0)
# A better option would be to check if the Class is of type Node
node = Node("A")
# while node:
# print(type(node))
while isinstance(node, Node):
    print(node.data)
    node = node.next


"""
3. Write a code segment that transfers items from a full array to a singly linked 
structure. The operation should preserve the ordering of the items.
​
"""

def array2node(p_array):
    # Takes each item in an array, in reverse order since our Node is LIFO oriented, and adds to the Node class
    # Instantiate our pointer for the Node class
    head = None
    # iterate for each index in the array, from the last item to the first
    for ind in range(len(p_array) - 1, -1, -1):
        # Add a Node object with the array's data to the pointer
        head = Node(p_array[ind], head)
    # return the pointer containing all of the nodes of the array's data
    return head

my_list = [x for x in range(1,6)]
pointer = array2node(my_list)

probe = pointer
while probe != None and 3 != probe.data:
    probe = probe.next
if probe != None:
    probe.data = 9

while pointer:
    print(pointer.data)
    pointer = pointer.next


