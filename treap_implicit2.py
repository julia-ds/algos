# You have an array a1=1,a2=2,...an=n and a sequence of queries: move elements from li to ri to front.
# For example, if the array is 2,3,6,1,5,4, after the query (2,4) the new order of elements in the array is 3,6,1,2,5,4.
# If, for example, the query (3,4) follows, the new order of elements is 1,2,3,6,5,4.
# Print the final order of elements in the array.
# Input
# The first line of the input file contains two integer numbers n and m (2≤n≤100000, 1≤m≤100000) — the number of
# elements and the number of queries. The following m lines contain queries, each line contains two integer numbers li
# and ri (1≤li≤ri≤n).
# Output
# Output n integer numbers — the order of elements in the final array, after executing all queries.
# Example
# input
# 6 3
# 2 4
# 3 5
# 2 2
# output
# 1 4 5 2 3 6

import sys
import random


class TreeNode:
    def __init__(self, key, priority):
        self.key = key
        self.left = None
        self.right = None
        self.priority = priority
        self.size = 1


class TreapImplicit:
    def __init__(self):
        self.v = None

    @staticmethod
    def get_priority():
        return random.randint(1, 2 ** 37)

    @staticmethod
    def fix_size(v):
        return get_size(v.left) + get_size(v.right) + 1

    def split(self, v, key):
        if v is None:
            return None, None
        if get_size(v.left) > key:
            t1, t2 = self.split(v.left, key)
            v.left = t2
            v.size = self.fix_size(v)
            return t1, v
        else:
            t1, t2 = self.split(v.right, key - get_size(v.left) - 1)
            v.right = t1
            v.size = self.fix_size(v)
            return v, t2

    def merge(self, t1, t2):
        if t1 is None:
            return t2
        elif t2 is None:
            return t1
        elif t1.priority > t2.priority:
            t1.right = self.merge(t1.right, t2)
            t1.size = self.fix_size(t1)
            return t1
        else:
            t2.left = self.merge(t1, t2.left)
            t2.size = self.fix_size(t2)
            return t2

    def insert(self, key, ind):
        new_node = TreeNode(key, self.get_priority())
        if self.v is None:
            self.v = new_node
        else:
            t1, t2 = self.split(self.v, ind - 1)
            self.v = self.merge(t1, new_node)
            self.v = self.merge(self.v, t2)

    def delete(self, ind):
        t1, t2 = self.split(self.v, ind)
        t1_left, t1_right = self.split(t1, ind - 1)
        self.v = self.merge(t1_left, t2)

    def replace_numbers(self, ind1, ind2):
        t1, t2 = self.split(self.v, ind2)
        t1_left, t1_right = self.split(t1, ind1 - 1)
        new_t = self.merge(t1_left, t2)
        self.v = self.merge(t1_right, new_t)


def get_size(v):
    if v is None:
        return 0
    else:
        return v.size


def show_structure(v):
    if v is not None:
        show_structure(v.left)
        sys.stdout.write(str(v.key) + ' ')
        show_structure(v.right)


tree = TreapImplicit()
n, m = list(map(int, sys.stdin.readline().split(' ')))
for i in range(n):
    tree.insert(i + 1, i)
for _ in range(m):
    ind1, ind2 = list(map(int, sys.stdin.readline().split(' ')))
    tree.replace_numbers(ind1 - 1, ind2 - 1)
show_structure(tree.v)