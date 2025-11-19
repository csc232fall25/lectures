import os
import time
import multiprocessing as mp

# NOTE: Processes do not share memory -- generally speaking, for security, no
#       process has access to any other process's data. Even if we put that
#       data into global variables, it cannot be shared across processes.
x = None
y = None


def f(x):
    # NOTE: A process is a running instance of a program. Every process has a
    #       unique process identifier, so if this program is run multiple
    #       times, it ought to receive a different identifier each time.
    time.sleep(1)
    print("f:", os.getpid())


def min_element(lst):
    global x
    x = min(lst)
    print("min:", os.getpid(), x)


def max_element(lst):
    global y
    y = max(lst)
    print("max:", os.getpid(), y)


def main():
    global x, y

    # NOTE: Here, the function f sleeps for 1 second to simulate some complex
    #       computation that takes 1 second to finish. If f is called twice in
    #       serial, those calls take 2 seconds to complete...
    # f(1)
    # f(2)

    lst = [2, -1, 9, 8, 5, 0, 8, 4]

    # NOTE: ...but if f is called twice in parallel, those calls take only 1
    #       second to complete since the second function call does not have to
    #       wait for the first to return.
    p1 = mp.Process(target=min_element, args=[lst])
    p2 = mp.Process(target=max_element, args=[lst])
    p1.start()
    p2.start()

    # NOTE: Once the processes we've created have started, they're executing
    #       in parallel, so there is no guarantee as to what order they finish.
    #       If we need to wait for them to finish, we can "join" with them.
    p1.join()
    p2.join()
    print("main:", os.getpid(), x, y)


# NOTE: It turns out that if we want to spawn more processes, the code that
#       does that needs be within a main block:
if __name__ == "__main__":
    main()