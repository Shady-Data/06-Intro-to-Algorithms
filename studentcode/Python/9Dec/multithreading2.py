'''
Run 10 threads

we can also now pass in an argument for seconds
'''

import threading
import time

start = time.perf_counter()

# def do_something():
#     print('Sleeping 1 second...')
#     time.sleep(1)
#     print('Done Sleeping...')

def do_something(seconds):
    print(f'Sleeping {seconds} second...')
    time.sleep(seconds)
    print('Done Sleeping...')

# initialize list of threads
threads = []

# set up loop to start 10 threads
for _ in range(10):
    t = threading.Thread(target=do_something, args=[1.5])
    t.start()
    threads.append(t)

for thread in threads:
    thread.join()

finish = time.perf_counter()

print(f'Finished in {finish - start} second(s)')