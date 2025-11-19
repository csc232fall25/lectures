import time
import multiprocessing as mp


def f(lst):
    total = 0

    for element in lst:
        # NOTE: For the sake of demonstration, suppose this was some more
        #       complex computation that took half a second to perform.
        time.sleep(0.5)
        total = total + element

    return total


def g(idx, lst):
    print(idx, lst)


def main():
    # NOTE: In data parallelism, a dataset is divided into subsets, each of
    #       which are processed simultaneously. Here, a list is divided into
    #       halves which we will eventually sum in parallel.
    lst = [2, -1, 8, 5, 0, 9, 8, 7]
    halves = [lst[:4], lst[4:]]

    # NOTE: In the map pattern, each element of a collection is mapped to a
    #       result by applying a function. Here, each half of the list is
    #       mapped to its sum.
    # print(list(map(f, halves)))

    # NOTE: A pool is a collection of "worker" processes waiting for something
    #       to do. In particular, because the map pattern is such a common use
    #       case, pools have a built-in function for parallelizing maps.
    with mp.Pool() as pool:
        print(pool.map(f, halves))

    # NOTE: The above is arguably inefficient; there is no point to using more
    #       processes than elements in the mapped collection. Additionally, if
    #       the mapped function needs more information, we need to starmap.
    with mp.Pool(processes = 2) as pool:
        pool.starmap(g, [(0, halves[0]), (1, halves[1])])


if __name__ == "__main__":
    main()