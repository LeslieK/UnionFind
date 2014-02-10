from itertools import combinations


def ThreeSum(int_list):
    """
    given n distinct ints, how many sum to 0?
    """
    triples = (t for t in combinations(int_list, 3) if sum(t) == 0)

    count = 0
    for t in triples:
        count += 1
    #print count

"""
python -m timeit -n 100 -s "import week1" "a=[30, -40, -20, -10, 40, 0, 10, 5];
week1.ThreeSum(a)"
"""
