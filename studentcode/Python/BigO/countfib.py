# prints the number of calls of a recursive Fibonacci function with problem sizes that double
# a working version since provided examples failed (no counter module)

def fib(n):
    global calls
    # Count the number of calls of the fib function
    calls += 1
    if n < 3:
        return 1
    else:
        return fib(n - 1) + fib(n - 2)

problemSize = 2
for _ in range(5):
    calls = 0
    # The start of the algorithm
    fib(problemSize)
    # The end of the algorithm
    print(f'{problemSize:12} - {calls:10}')
    problemSize *= 2