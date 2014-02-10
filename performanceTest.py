import ErdosRenyi as ER
import time


def performance(algo):
    """
    algo: the UnionFind algorithm: QF, QU, WQU, WQUH, WQUPC
    T: the number of trials
    N: the starting number of sites
    """
    T = raw_input("Enter number of trials: ")
    T = int(T)
    N = raw_input("Enter starting N: ")
    N = int(N)
    start = time.time()
    connections, avg_connections = ER.main(N, algo)
    prev_elapsed_time = time.time() - start
    T -= 1
    while T > 0:
        N = 2 * N
        start = time.time()
        connections, avg_connections = ER.main(N, algo)
        elapsed_time = time.time() - start
        time_ratio = elapsed_time / prev_elapsed_time
        print "{}\t{}\t{}\t\t{}".format(N, connections, avg_connections,
                                        time_ratio)
        prev_elapsed_time = elapsed_time
        T -= 1


def compare_algos(algo, algo2):
    if algo2 is None:
        return
    T = raw_input("Enter number of trials: ")
    T = int(T)
    N = raw_input("Enter starting N: ")
    N = int(N)
    print "N\talgo1:algo2"
    print
    while T > 0:
        N, algo_to_algo2_ratio = ER.main(N, algo, algo2)
        print "{}\t{}".format(N, algo_to_algo2_ratio)
        N = 2 * N
        T -= 1


def main(func_num):
    test = {"1": performance, "0": compare_algos}
    if func_num == "0":
        algo = raw_input("Enter algo: ")
        algo2 = raw_input("Enter another algo: ")
        test[func_num](algo.upper(), algo2.upper())
    else:
        algo = raw_input("Enter algo: ")
        test[func_num](algo.upper())

########################################################
if __name__ == "__main__":
    func_num = \
        raw_input("Enter test [0: compare algos  1: test single algo]: ")
    while func_num not in {"0", "1"}:
        func_num = \
            raw_input("Enter test [0: compare algos  1: test single algo]: ")
    main(func_num)

