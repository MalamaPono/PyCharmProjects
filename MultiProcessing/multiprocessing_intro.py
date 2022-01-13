# Threading doesn't really show an improvement on CPU bound problems because all those threads
# are still running on one process which doesn't really affect computational problems that processes (CPU) work on

# Multiprocessing on the other hand, spreads the work out to multiple processes (CPU) on our machine.
# This allows us to use multiprocessing to speed up our programs on CPU bound tasks and IO bound tasks.

# In these cases it is really up to our computers hardware to decide whether to use multiprocessing or threading.

# The amount of processes you can run depends on the number of cores you have on your CPU
# However you may be able to run more processes than cores on your CPU because computers actually
# now have ways to switch on and off cores to allow for more processes.
#
import time
import multiprocessing

def do_something(seconds):
    print(f'Sleeping {seconds} second(s)')
    time.sleep(seconds)
    print("Done sleeping")



def main():
    start = time.perf_counter()

    processes = []

    for _ in range(10):
        p = multiprocessing.Process(target=do_something, args=[1.5])
        p.start()
        processes.append(p)

    for process in processes:
        process.join()

    finish = time.perf_counter()

    print(f'Finished in {round(finish - start, 2)} second(s)')

if __name__ == '__main__':
    main()