'''
Binary Tree is a tree data structure in which each node has at most two children which are left child and right child

     - top node is root

Complete binary tree - every level, except possibly the last, is completely filled and all nodes in the last level are as far left as possible

Full binary tree - A full binary tree (referred to as a proper or plane binary tree) is a tree where every node except the leaves has two children
    
Tree Traversal - process of visiting (checking and/or updating) each node in a tree data structure, exactly once

Unlike linked lists, one-dimensional arrays, etc., which are traversed in linear order, trees may be traveresed in multiple-ways.

depth-first order, pre-order, post-order, in-order

pre-order - check if the current node is empty
            display the data part of the root or current node
            traverse the left subtree by recursively calling the pre-order function
            traverse the right subtree by recursively calling the pre-order function

in-order -  check if the current node is empty
            traverse the left subtree by recursively calling the in-order function
            display the data part of the root or current node
            traverse the right subtree by recursively calling the in-order function

post-order -check if the current node is empty
            traverse the left subtree by recursively calling the in-order function
            traverse the right subtree by recursively calling the in-order function
            display the data part of the root or current node
'''


class TreeNode:
    def __init__(self, value):
        self.value = value
        self.left = None
        self.right = None
    
class BinaryTree:
    def __init__(self, root):
        self.root = TreeNode(root)

    def print_tree(self, traversal_type):
        if traversal_type == 'preorder':
            return self.preorder_print(self.root, '') # start with an empty string that will fill out
        if traversal_type == 'inorder':
            return self.inorder_print(self.root, '') # start with an empty string that will fill out
        if traversal_type == 'postorder':
            return self.postorder_print(self.root, '') # start with an empty string that will fill out

    def preorder_print(self, start, traversal):
        # root --> left --> right
        if start:
            traversal += (str(start.value) + '-')
            traversal = self.preorder_print(start.left, traversal)
            traversal = self.preorder_print(start.right, traversal)
        return traversal

    def inorder_print(self, start, traversal):
        # left --> root --> right
        if start:
            traversal = self.inorder_print(start.left, traversal)
            traversal += (str(start.value) + '-')
            traversal = self.inorder_print(start.right, traversal)
        return traversal

    def postorder_print(self, start, traversal):
        # left --> right --> root
        if start:
            traversal = self.postorder_print(start.left, traversal)
            traversal = self.postorder_print(start.right, traversal)
            traversal += (str(start.value) + '-')
        return traversal

bt = BinaryTree('D')
bt.root.left = TreeNode('B')
bt.root.left.left = TreeNode('A')
bt.root.left.right = TreeNode('C')
bt.root.right = TreeNode('F')
bt.root.right.left = TreeNode('E')
bt.root.right.right = TreeNode('G')

print(bt.print_tree('preorder'))
print(bt.print_tree('inorder'))
print(bt.print_tree('postorder'))