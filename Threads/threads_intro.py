# Threading allows code to be run concurrently with more than one instance.
# Should be used when you want to significantly speed up your program.
# Usually useful for IO bound problems when we are waiting around to read
# input and output or other networking related problems. Not really for CPU bound problems.

# Threading doesn't actually run the code at the same time, but simply moves and executes other parts
# of the script when it becomes IO bound and is waiting for the reading and or writing to finish.

# CPU bound problems are usually counteracted by multiprocessing which allows us to run code in parallel
# by using up more cores in our cpu to do more tasks. Running these tasks at the same time allows us
# to use more cpu space and try to use as much cpu as we can.

import time
import threading

start = time.perf_counter()

def do_something():
    print('Sleeping 1 second...')
    time.sleep(1)
    print('Done sleeping...')

t1 = threading.Thread(target=do_something)
t2 = threading.Thread(target=do_something)

t1.start()
t2.start()

t1.join()
t2.join()
# makes sure these threads finish here first before moving to the following code below

finish = time.perf_counter()

print(f'Finished in {round(finish-start,2)} second(s)')
