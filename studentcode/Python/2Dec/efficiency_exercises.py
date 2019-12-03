"""
1. Write a tester program that counts and displays the number of iterations 
    of the following loop: 
    
    while problemSize > 0:
        problemSize = problemSize // 2

2. Run the program you created in Exercise 1 using problem sizes of 
    1000, 2000, 4000, 10,000, and 100,000. As the problem size doubles 
    or increases by a factor of 10, what happens to the number of iterations?

3. The difference between the results of two calls of the function time.time() 
    is an elapsed time. Because the operating system might use the CPU for part 
    of this time, the elapsed time might not reflect the actual time that a 
    Python code segment uses the CPU. Browse the Python documentation for an 
    alternative way of recording the processing time, and describe how this 
    would be done.
​
"""

# import time
import timeit

def main():
    problemSizes = [1000, 2000, 4000, 10000, 100000, 200000, 10000000, 100000000, 1000000000, 10000000000, 100000000000, 1000000000000, 10000000000000]
    for probsize in problemSizes:
        setup = '''\nloops = 0\nproblemSize = ''' + str(probsize) +'''\nwhile problemSize > 0:\n\tproblemSize = problemSize // 2\n\tloops += 1\nprint(loops)'''
        print(timeit.timeit(setup=setup))
    #     problemSize = probsize
    #     iteration = 0
        # start = time.time()
        # while problemSize > 0:
        #     problemSize = problemSize // 2
        #     iteration += 1
        # elapsed = time.time() - start
        # print(f'{problemSizes[ind]:12} - {iteration} - {elapsed:12.10f}')

main()