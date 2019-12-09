'''
Using multithread module is the old way
Python 3.2 introduced thread pool executor

No longer need threading module
we use concurrent.futures module instead
'''

import concurrent.futures
import time

start = time.perf_counter()

def do_something(seconds):
    print(f'Sleeping {seconds} second...')
    time.sleep(seconds)
    return 'Done Sleeping...'

# using a context manager
with concurrent.futures.ThreadPoolExecutor() as executor:
    # submit schedules a function to be executed one at a time and returns a future object
    # f1 = executor.submit(do_something, 1)
    # f2 = executor.submit(do_something, 1)
    
    # print(f1.result())
    # print(f2.result())

    results = [executor.submit(do_something, 1) for _ in range(10)]

    # to get the results we can use another funtion, as_completed(), from future object that gives us an iterator
    for f in concurrent.futures.as_completed(results):
        print(f.result())

finish = time.perf_counter()

print(f'Finished in {finish - start} second(s)')