'''
Prove that these are actually coming in as completed,
    lets pass in a range of seconds

Start 5 second thread first, but since we used as_completed() method it prints the results
    in the order they are completed

With the submit() method, it submits each function one at a time,
    so we can use the submit() method on an entire list by using map
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
    seconds_list = [5, 4, 3, 2, 1]
    # results = [executor.submit(do_something, sec) for sec in seconds_list]
    # results = [executor.submit(do_something, sec) for sec in range(5, 0, -1)]

    # map will apply the function do_something() to every item in the seconds_list
    # instead of running the results as complete, map returns in the order that they were started

    results = executor.map(do_something, seconds_list)

    # to get the results we can use another funtion, as_completed(), from future object that gives us an iterator
    for result in results:
        print(result)

finish = time.perf_counter()

print(f'Finished in {finish - start} second(s)')