'''
Prove that these are actually coming in as completed,
    lets pass in a range of seconds

Start 5 second thread first, but since we used as_completed() method it prints the results
    in the order they are completed
'''

import concurrent.futures
import time

start = time.perf_counter()

def do_something(seconds):
    print(f'Sleeping {seconds} second...')
    time.sleep(seconds)
    return f'Done Sleeping...{seconds}'

# using a context manager
with concurrent.futures.ThreadPoolExecutor() as executor:
    # submit schedules a function to be executed one at a time and returns a future object
    # f1 = executor.submit(do_something, 1)
    # f2 = executor.submit(do_something, 1)
    
    # print(f1.result())
    # print(f2.result())
    # seconds_list = [5, 4, 3, 2, 1]
    # results = [executor.submit(do_something, sec) for sec in seconds_list]
    results = [executor.submit(do_something, sec) for sec in range(5, 0, -1)]

    # to get the results we can use another funtion, as_completed(), from future object that gives us an iterator
    for f in concurrent.futures.as_completed(results):
        print(f.result())

finish = time.perf_counter()

print(f'Finished in {finish - start} second(s)')