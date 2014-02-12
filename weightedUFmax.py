
"""
Union-find with specific canonical element.
Add a method find() to the union-find data type
so that find(i) returns the largest element in
the connected component containing i.
The operations, union(), connected(), and find()
should all take logarithmic time or better.

For example, if one of the connected components is
{1,2,6,9}, then the find() method should return 9
for each of the four elements in the connected components.

for example:
uf = WeightedQuickUnionUF(20)
uf.union(0, 3)
uf.union(0, 5)
uf.find(0) => returns 5
uf.find(3) => returns 5
uf.find(5) => returns 5

"""


class WeightedQuickUnionUF(object):
    def __init__(self, N):
        self._id = [i for i in range(N)]
        self._size = [1 for i in range(N)]
        self._count = N
        self._accesscnt = 0
        self._maxElem = [i for i in range(N)]

    def newSite(self):
        new_site = sum(self._size)
        self._id.append(new_site)
        self._size.append(1)
        self._count += 1
        self._maxElem.append(new_site)
        return new_site

    def count(self):
        return self._count

    def connected(self, p, q):
        return self.find(p) == self.find(q)

    def find(self, p):
        """
        returns maximum element in component
        """
        def helper(self, maxnum, p):
            if p == self._id[p]:
                if maxnum > self._maxElem[p]:
                    print maxnum, self._maxElem[p], p
                    self._maxElem[p] = maxnum
                return self._maxElem[p]
            else:
                if self._id[p] > maxnum:
                    maxnum = self._id[p]
                return helper(self, maxnum, self._id[p])
        return helper(self, self._maxElem[p], p)

    def union(self, p, q):
        self._accesscnt = 0
        i = self.find(p)
        j = self.find(q)
        if i == j:
            # already connected
            return
        si = self._size[i]
        sj = self._size[j]
        if si < sj or (si == sj and i < j):  # modified
            self._id[i] = j
            self._size[j] = sj + si
            self._size[i] = 0
            # modified
            self._maxElem[j] = max(self._maxElem[i], self._maxElem[j])
        else:
            self._id[j] = i
            self._size[i] = si + sj
            self._size[j] = 0
            # modified
            self._maxElem[i] = max(self._maxElem[i], self._maxElem[j])
        self._count -= 1
        self._accesscnt += 5

    def accesscnt(self):
        return self._accesscnt

"""
Successor with delete.
Given a set of N integers S={0,1,...,N−1} and a random sequence of commands:
remove(x) : removes x from the set
find(x) :
finds y such that y is the immediate successor of x (if x is not in set)
or y == x (if x is in the set)

s = SuccessorWithDelete(20)
s.find(5) => returns 5
s.remove(5)
s.find(5) => returns 6

s.unremove(5)  (This means it is not truly deleted!)
s.find(5) => returns 5
"""


class SuccessorWithDelete(object):
    def __init__(self, alist):
        N = len(alist)
        self._id = alist
        self._size = [1 for i in range(N)]
        self._maxElem = list(alist)

    def _find(self, p):
        """
        returns largest number in component
        """
        def helper(self, maxnum, p):
            """
            climb tree from p
            save largest number seen along the way in maxnum
            if maxnum > number root has seen so far (._maxElem[p]),
            then store maxnum in maxElem[p]
            """
            if p == self._id[p]:
                if maxnum > self._maxElem[p]:
                    print maxnum, self._maxElem[p], p
                    self._maxElem[p] = maxnum
                return self._maxElem[p]
            else:
                if self._id[p] > maxnum:
                    maxnum = self._id[p]
                return helper(self, maxnum, self._id[p])
        return helper(self, self._maxElem[p], p)

    def _findRoot(self, p):
        """
        returns root of p
        """
        if p != self._id[p]:
            return self._findRoot(self._id[p])
        return p

    def remove(self, p):
        """
        connect root(p) and root(p+1)
        """
        if not self.inSet(p):
            return "not in set"
        if p == len(self._id) - 1:
            self._id[p] = None
            self._last_removed = p
            return
        if self._id[p + 1] is None:
            self._id[p] = None
            self._last_removed = p
            return
        else:
            i = self._findRoot(p)
            j = self._findRoot(p + 1)
            sp = self._size[i]
            sq = self._size[j]
            if sp < sq or (sp == sq and i < j):  # modified
                self._id[i] = j
                self._size[j] = sq + sp
                self._size[i] = sq + sp
                self._maxElem[j] = max(self._maxElem[i], self._maxElem[j])
            else:
                self._id[j] = i
                self._size[i] = sp + sq
                self._size[j] = sp + sq
                self._maxElem[i] = max(self._maxElem[i], self._maxElem[j])
        self._last_removed = p

    def unremove(self, p=None):
        if p is None:
            p = self._last_removed
        if self.inSet(p):
            return p, " is in set."
        self._id[p] = p

    def find(self, p=None):
        # return largest number in p+1 component
        if p is None:
            p = self._last_removed
        if not self._id[p]:
            return "Upperbound of set. No successor."
        return self._find(p)

    def inSet(self, p):
        """
        True if p is max number in component
        """
        if p >= len(self._id) - 1 or p < 0:
            return False
        return self._id[p] is not None and p == self._find(p)
