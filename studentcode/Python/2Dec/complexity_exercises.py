"""
1. Assume that each of the following expressions indicates the number of 
operations performed by an algorithm for a problem size of n. Point out 
the dominant term of each algorithm and use big-O notation to classify it. 
​
    a. 2^n - 4n^2 + 5n
    O(2^n) - exponential
    b. 3n^2 + 6
    O(n^2) - quadratic
    c. n^3 + n^2 - n
    O(n^3) - polynomial
​
2. For problem size n, algorithms A and B perform n^2 and (1/2)n^2 + (1/2)n 
instructions, respectively. Which algorithm does more work? Are there particular 
problem sizes for which one algorithm performs significantly better than the 
other? Are there particular problem sizes for which both algorithms perform 
approximately the same amount of work?

    Algorithm B does more work and algorithm A is better for smaller problem sizes???
​
3. At what point does an n^4 algorithm begin to perform better than a 2^n algorithm?

    n=2
    2^4 == 16 > 2^2 == 4
    n=3
    3^4 == 81 > 2^3 == 8
    n=10
    10^4 == 10000 > 2^10 == 1024
    n=16
    16^4 == 65536 == 2^16 == 65536
    n=17
    17^4 == 83521 < 2^17 == 131072

"""
# print(17**4)
# print(2**17)