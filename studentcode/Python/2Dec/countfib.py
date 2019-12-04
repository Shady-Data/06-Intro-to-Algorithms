# prints the number of calls of a recursive Fibonacci function with problem sizes that double
# a working version since provided examples failed (no counter module)

# import timeit
import time

# initialize the global calls variable
# this variable stores the number of times (increments) the recursive fibonacci function is called
calls = 0
def fib(n):
    # pull the global calls variable into the scope of the function
    global calls
    # Count the number of calls of the fib function
    # increment the calls variable by 1 for each time the function is called
    calls += 1
    if n < 3:
        return 1
    else:
        return fib(n - 1) + fib(n - 2)

# Set the size of the problem
problemSize = 2
for _ in range(5):
    # reset the number of calls for each run
    calls = 0
    start = time.time()
    # The start of the algorithm
    fib(problemSize)
    # The end of the algorithm
    elapsed = time.time() - start
    # print(f'{problemSize:12} - {calls:10}')
    print(f'{problemSize:8} - {calls:20,} - {elapsed:15.5f}')
    # double the problem size
    problemSize *= 2

# setup = '''\ncalls = 0\ndef fib(n):\n\tglobal calls\n\tcalls += 1\n\tif n < 3:\n\t\treturn 1\n\telse:\n\t\treturn fib(n - 1) + fib(n - 2)\nproblemSize = 2\nfor _ in range(7):\n\tcalls = 0\n\tfib(problemSize)\n\tprint(f"{problemSize:8} - {calls:18}")\n\tproblemSize *= 2'''
# timeit.timeit(setup=setup)