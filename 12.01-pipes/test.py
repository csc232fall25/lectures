import os
import multiprocessing as mp


def min_element(lst, pipe_end):
    x = min(lst)
    print("min:", os.getpid(), x)
    pipe_end.send(x)


def max_element(lst, pipe_end):
    y = max(lst)
    print("max:", os.getpid(), y)
    pipe_end.send(y)


def main():
    # NOTE: Processes do not share memory -- generally speaking, for security,
    #       no process has access to any other process's data. Even if we put
    #       that data into global variables, it is not shared across processes.
    # global x, y

    lst = [2, -1, 9, 8, 5, 0, 8, 4]

    # NOTE: A pipe is essentially a temporary file managed by the OS: like a
    #       file, a pipe is accessible by multiple processes; unlike a file,
    #       a pipe can be stored in memory and is not publicly visible.
    parent_end1, child_end1 = mp.Pipe()

    # NOTE: If both children used the same pipe, we would have no way of
    #       knowing which data was sent by which child -- generally speaking,
    #       we need a separate pipe for each child.
    parent_end2, child_end2 = mp.Pipe()

    child1 = mp.Process(target=min_element, args=[lst, child_end1])
    child2 = mp.Process(target=max_element, args=[lst, child_end2])
    child1.start()
    child2.start()

    # NOTE: Any data sent into the pipes by the children can then be recevied
    #       from the corresponding ends of the pipes within the parent. Here,
    #       we receive before we join in order to get the data ASAP.
    x = parent_end1.recv()
    y = parent_end2.recv()

    child1.join()
    child2.join()
    print("main:", os.getpid(), x, y)


if __name__ == "__main__":
    main()
