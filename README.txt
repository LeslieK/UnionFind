1. To run a comparison test between 2 algorithms or to test the performance of a single algorithm, enter:

C> python performanceTest.py

If you get a divide by 0 error, choose a larger N (> 64).

algorithms:
QF : quick find
QU : quick union
WQU: weighted quick union (uses tree size as "weight")
WQUH : weighted quick union (uses tree height as "weight")
WQUPC : weighted quick union with path compression (uses tree height as "weight")

C> python performanceTest.py
Enter test:      [0: compare algos  1: test single algo]: default is 1: 0
Enter algo: wquh
Enter another algo: wqupc
Enter number of trials: 8
Enter starting N (2 - 500): 100
N         algo1:algo2 (ratio of running times)

64        0.999761620977
128       0.666613685131
256       1.0
512       1.20003814792
1024      1.0
2048      0.999991778682
4096      0.999995665122
8192      1.02439237138
C>

In the following example, as N doubles, the ratio of current_time:prev_time quadruples!
C:> python performanceTest.py
Enter test:      [0: compare algos  1: test single algo]: default is 1: 1
Enter algo: qf
Enter number of trials: 8
Enter starting N: 32
N         num_connections   avg_connections   curr_time : prev_time
64        132               2.0625            2.99952324195
128       393               3.0703125         2.0
256       739               2.88671875        2.0
512       1913              3.736328125       1.58332671064
1024      3225              3.1494140625      1.05262761632
2048      10058             4.9111328125      2.95000357628
4096      15964             3.8974609375      1.59322164032
C:>

2. To generate random connections for an NxN grid, make the connections, and visualize the results:
C:> python UFanimation.py
Enter N [default: 5]: 8
Enter algo [default: WQUH]:

At this point, a figure pops up (requires matplotlib and numpy). Connections are made between nodes in the grid until all nodes are connected. Need to change this so the graph displays all plotted lines rather than just the last one.

