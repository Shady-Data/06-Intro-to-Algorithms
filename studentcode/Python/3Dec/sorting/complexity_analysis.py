'''
************** Complexity Analysis **************

complexity analysis -   a method of demtermining the efficiency of algorithms that allows you to rate them independently of platform-dependent timings or impractical instruction counts

order of complexity -   The difference in performance of your algorithms

linear -    grows in direct porportion to the size of the problem

quadratic - grows as a function of the square of the problem size

logarithmic -   proportional to the log base 2 of the problem size

polynomial time algorithm - grows at a rate of n raised to the k

exponential -   a growth rate of 2 raised to the n. These are impractical to run with large problem sizes

************** Big-O Notation **************

"O" is the order of complexity

dominant -  the amount of work in an algorithm that becomes so large that you can ignore the amount of work represented by the other terms

            (1/2)n^2-(1/2)n
            n^2 is dominant here.

            Represented with Big-O notation:
            O(n^2)

Constant O(1)
    - Time taken is independent of the amount of data
    - Stack push, pop and peek, Queue, dequeue and enqueue; Insert a node in to a linked list

Linear O(n)
    - Time taken is directly proportional to the amount of data
    - Linear search; counting items in a list; compare a pair of strings

Quadratic O(n^2)
    - Time taken is proportional to the amount of data squared, twice as much data takes 4 times as long to process, poor scalability
    - Bubble Sort; Selection Sort; Insertion Sort; Traverse a 2D array

Polynomial O(n^k)
    - Time taken is proportional to the amount of data raised to the power of a constant

Logarithmic O(log n)
    - Time taken is proportional to the logarithm of the amount of data, good scalability
    - Binary Search a sorted list; Search a binary tree; Divide and conquer algorithm approaches

Linearithmic O(n log n)
    - Time taken is proportional  to the logarithm of the amount of data, multiplied by the amount of data

Exponential O(k^n)
    - Time taken is proportional to a constant raised to the power of the amount of data, very poor scalability almost immediately.
    - if constant k is 10, then one extra item of data will slow it down 10 times

Logarithms - The inverse of exponentiation

    Generally
        x^z = y             log base x of y = z

        2^0 = 1             log base 2 of 1 = 0
        2^1 = 2             log base 2 of 2 = 1
        2^2 = 4             log base 2 of 4 = 2
        2^3 = 8             log base 2 of 8 = 3
        2^4 = 16            log base 2 of 16 = 4

        10^4 = 10000        log base 10 of 10000 = 4

        notice that each number we're calculating the log of is twice as much as the previous number
        but each log is only 1 bigger than the previous value

'''