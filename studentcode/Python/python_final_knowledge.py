"""
Collections:

    Multiple Choice:

        1. Examples of linear collections are:
            a. Sets and trees
            (b. Lists and stacks)

        2. Examples of unordered collections are:
            a. Queues and lists
            (b. Sets and dictionaries)
        
        3. A hierarchical collection can represent a:
            a. Line of customers at a bank
            (b. File directory system)

        4. The == operation for two lists must:
            (a. Compare pairs of items at each position for equality)
            b. Merely verify that each item in one list is also in the other list

        5. The map function creates a sequence of the:
            a. Items in a given collection that pass a Boolean test
            (b. Results of applying a function to the items in a given collection)

Searching, Sorting and Complexity:

    Multiple Choice:

        1. Timing an algorithm with different problem sizes:
            a. Can give you a general idea of the algorithm's run-time behavior
            (b. Can give you an idea of the algorithm's run-time behavior on a
                particular hardware platform and a particular software platform)
        
        2. Counting instructions:
            (a. Provide the same data on different hardware and software platforms)
            b. Can demonstrate the impracticality of exponential algorithms 
                with large problem sizes

        3. The expressions O(n), O(n^2), and O(k^n) are, respectively:
            a. Exponential, linear, and quadratic
            (b. Linear, quadratic, and exponential)
            c. Logarithmic, linear and quadratic

        4. A binary search assumes that the data are:
            a. Arranged in no particular order
            (b. Sorted)

        5. A selection sort makes at most:
            a. n^2 exchanges of data items
            (b. n exchanges of data items)

        6. The best-case behavior of insertion sort and modified bubble sort is:
            (a. Linear)
            b. Quadratic
            c. Exponential
        
        7. An example of an algorithm whose best-case, average-case, and worst-case
            behaviors are the same is:
            a. Sequential search
            (b. Selection sort)
            c. Quicksort

        8. Generally speaking, it is better to:
            a. Tweak an algorithm to shave a few seconds of running time
            (b. Choose an algorithm with the lowest order of computational complexity)
        
        9. The recursive Fibonacci function makes approximately:
            a. n^2 recursive calls for problems of a large size n
            (b. 2^n recursive calls for problems of a large size n)

Linked Structures:
    
    Multiple Choice:

        1. This linked structure contains links running both directions:
            a. Singly linked list
            (b. Doubly linked list)
        
        2. This link allows the user to access the last item directly:
            a. Empty link
            b. Head link
            (c. Tail link)

        3. The basic unit of representation in a linked structure:
            (a. Node)
            b. Container
            c. Collection

        4. We do this operation to visit each node:
            a. Stepping
            (b. Traversal)
        
        5. An empty node pointer is represented as:
            (a. None)
            b. Empty
            c. Nought
        
        6. This points to the node following the current node:
            a. probe.data
            (b. probe.next)
            c. probe.head

        7. Doubly linked nodes usually have all of these attributes with the
            exception of:
            a. next
            b. prev
            c. data
            (d. index)

        8. Nodes in a singly linked structure contain Data and:
            (a. next)
            b. prev
            c. cell

        9. A doubly linked structure allows the programmer to move:
            (a. To the next node or the previous node from a given node)
            b. To the next node only from a given node

Stacks

    Multiple Choice

        1. An example of a stack is:
            a. Customers waiting in a checkout line
            (b. A deck of playing cards)
            c. A file directory system
            d. A line of cars at a tollbooth
            e. Laundry in a hamper

        2. The operations that modify a stack are called:
            a. Add and remove
            (b. Push and pop)

        3. Stacks are also known as:
            a. First-in first-out data structures
            (b. Last-in first-out data structures)

Queues

    Multiple Choice

        1. An example of a queue is:
            (a. Customers waiting in a checkout line)
            b. A deck of playing cards
            c. A file directory system
        
        2. The operations that modify a queue are:
            a. Add and remove
            (b. Push and pop)

        3. Queues are also known as:
            (a. First-in first-out data structures)
            b. Last-in first-out data structures

Trees

    Multiple Choice

        1. The distinguished node at the beginning or the top of a tree is called:
            a. Head node
            (b. Root node)
            c. Leaf node

        2. A node without children is called a:
            a. Single node
            (b. Leaf node)

        3. Each level k in a full binary tree contains:
            a. 2k nodes
            (b. 2^k + 1 nodes)
            c. 2^k - 1 nodes
        
        4. Assume that data are inserted into a binary search tree in the order 
            DBACFEG. Preorder traversal would return these data in the order:
            (a. DBACFEG)
            b. ABCDEFG

        5. Assume that data are inserted into a binary search tree in the order 
            DBACFEG. Inorder traversal would return these data in the order:
            a. DBACFEG
            (b. ABCDEFG) 

Regular Expressions:

    Multiple Choice

        1. To use the regular expression module you have to import:
            (a. re)
            b. regex
            c. regularexpressions

        2. In order to look at every regex match as a list of iterable objects you use:
            a. re.search()
            (b. re.finditer())
            c. re.compile()

        3. The meta character in regex to match any word character:
            a. \d
            (b. \w)
            c. \s

        4. The meta character in regex to match any whitespace character:
            a. \d
            b. \w
            (c. \s)

        5. This quantifier means to match 0 or more:
            (a. *)
            b. +
            c. ?
        
        6. This quantifier means to match 0 or one:
            a. *
            b. +
            (c. ?)

        7. This quantifier means to match 1 or more:
            a. *
            (b. +)
            c. ?

Recursion

    Multiple Choice

        1. A recursive function _______________.
            a. calls a different function
            b. abnormally halts the program
            (c. calls itself)
            d. can only be called once

        2. A function is called once from a program’s main function, and then it calls itself four
        times. The depth of recursion is _______________.
            a. one
            (b. four)
            c. five
            d. nine

        3. The part of a problem that can be solved without recursion is the _______________
        case.
            (a. base)
            b. solvable
            c. known
            d. iterative

        4. The part of a problem that is solved with recursion is the _______________case.
            a. base
            b. iterative
            c. unknown
            (d. recursive)

        5. When a function explicitly calls itself it is called _______________ recursion.
            a. explicit
            b. modal
            (c. direct)
            d. indirect

        6. When function A calls function B, which calls function A it is called _______________
        recursion.
            a. implicit
            b. modal
            c. direct
            (d. indirect)

        7. Any problem that can be solved recursively can also be solved with a _______________.
            a. decision structure
            (b. loop)
            c. sequence structure
            d. case structure

           
"""