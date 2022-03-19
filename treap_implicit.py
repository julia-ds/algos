# Learn how to quickly do two operations with an array: add i x - add after the i-th element x (0≤i≤n)
# del i - remove the i-th element (1≤i≤n)
# Input data
# On the first line n0 and m (1≤n0,m≤10**5) are the length of the original array and the number of queries.
# On the second line, n0 integers from 0 to 10**9 - 1 are the original array. Then m lines containing requests.
# It is guaranteed that the requests are correct: for example, if you are asked to remove the i-th element,
# it is definitely there.
# Output
# Print the final state of the array. On the first line, the number of elements, on the second line, the array itself.
# Example
# input
# 3 4
# 1 2 3
# del 3
# add 0 9
# add 3 8
# del 2
# output
# 3
# 9 2 8

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
array = list(map(int, sys.stdin.readline().split(' ')))
for i in range(n):
    tree.insert(array[i], i)
for _ in range(m):
    inp = sys.stdin.readline().split(' ')
    if inp[0] == 'add':
        tree.insert(int(inp[2]), int(inp[1]))
    elif inp[0] == 'del':
        tree.delete(int(inp[1]) - 1)
    else:
        pass
sys.stdout.write(str(get_size(tree.v)) + '\n')
show_structure(tree.v)