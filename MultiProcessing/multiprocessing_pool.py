import concurrent.futures
import time

def do_something(seconds):
    print(f'Sleeping {seconds} second(s)')
    time.sleep(seconds)
    return f"Done sleeping {seconds}"

def main():
    start = time.perf_counter()

    # context managers automatically join all threads or processes before moving on from the code after the context manager
    with concurrent.futures.ProcessPoolExecutor() as executor:
        seconds = [5,4,3,2,1]
        # returns results as future objects that has a bunch of methods to check in how the function performed
        results = [executor.submit(do_something,sec) for sec in seconds]
        # loops through the results as they are completed
        for f in concurrent.futures.as_completed(results):
            print(f.result())

        # # this map method returns the raw results of the function in the order that the were started
        # results = executor.map(do_something,seconds)
        # for result in results:
        #     print(result)

    finish = time.perf_counter()

    print(f'Finished in {round(finish - start, 2)} second(s)')

if __name__ == '__main__':
    main()