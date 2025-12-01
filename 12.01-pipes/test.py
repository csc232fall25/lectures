import os
import multiprocessing as mp

# NOTE: Processes do not share memory -- generally speaking, for security, no
#       process has access to any other process's data. Even if we put that
#       data into global variables, it cannot be shared across processes.
x = None
y = None


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

    lst = [2, -1, 9, 8, 5, 0, 8, 4]

    p1 = mp.Process(target=min_element, args=[lst])
    p2 = mp.Process(target=max_element, args=[lst])
    p1.start()
    p2.start()

    p1.join()
    p2.join()
    print("main:", os.getpid(), x, y)


if __name__ == "__main__":
    main()
