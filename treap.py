# Implement a balanced binary search tree.
# Input
# The input contains several operations with the tree and their amount does not exceed 10**5.
# Еvery line contains one of the following operations:
# insert 𝑥 — insert key 𝑥 into the tree. If there is a key 𝑥 in the tree already, do nothing;
# delete 𝑥 — remove key 𝑥 from the tree. If there is no key 𝑥 in the tree, do nothing;
# exists 𝑥 — if there is a key 𝑥 in the tree, output "true", otherwise output "false";
# next 𝑥 — output the smallest key in the tree that is strictly larger than 𝑥, or "none" if there's no such key;
# prev 𝑥 — output the largest key in the tree that is strictly less than 𝑥, or "none" if there's no such key.
# All keys are integers no greater than 109 by absolute value.
# Output
# Output results of all operations exists, next, prev.
# Example
# input
# insert 2
# insert 5
# insert 3
# exists 2
# exists 4
# next 4
# prev 4
# delete 5
# next 4
# prev 4
# output
# true
# false
# 5
# 3
# none
# 3

import sys
import random


class TreeNode:
    def __init__(self, key, priority):
        self.key = key
        self.left = None
        self.right = None
        self.priority = priority


class Treap:
    def __init__(self):
        self.v = None

    @staticmethod
    def get_priority():
        return random.randint(1, 2 ** 37)

    def split(self, v, key):
        if v is None:
            return None, None
        if v.key > key:
            t1, t2 = self.split(v.left, key)
            v.left = t2
            return t1, v
        else:
            t1, t2 = self.split(v.right, key)
            v.right = t1
            return v, t2

    def merge(self, t1, t2):
        if t1 is None:
            return t2
        elif t2 is None:
            return t1
        elif t1.priority > t2.priority:
            t1.right = self.merge(t1.right, t2)
            return t1
        else:
            t2.left = self.merge(t1, t2.left)
            return t2

    def insert(self, key):
        new_node = TreeNode(key, self.get_priority())
        if self.v is None:
            self.v = new_node
        else:
            t1, t2 = self.split(self.v, key - 1)
            self.v = self.merge(t1, new_node)
            self.v = self.merge(self.v, t2)

    def delete(self, key):
        t1, t2 = self.split(self.v, key)
        t1_left, t1_right = self.split(t1, key - 1)
        self.v = self.merge(t1_left, t2)


def next(v, x):
    root = v
    res = None
    while root is not None:
        if root.key > x:
            res = root.key
            root = root.left
        else:
            root = root.right
    return res


def prev(v, x):
    root = v
    res = None
    while root is not None:
        if root.key < x:
            res = root.key
            root = root.right
        else:
            root = root.left
    return res


def exists(v, x):
    if v is None:
        return False
    else:
        if v.key == x:
            return True
        elif x < v.key:
            return exists(v.left, x)
        else:
            return exists(v.right, x)


tree = Treap()
stdin = sys.stdin.readlines()
for inp in stdin:
    inp = inp.split(' ')
    if inp[0] == 'insert':
        bst = tree.insert(int(inp[1]))
    elif inp[0] == 'delete':
        tree.delete(int(inp[1]))
    elif inp[0] == 'exists':
        sys.stdout.write(str(exists(tree.v, int(inp[1]))).lower() + '\n')
    elif inp[0] == 'next':
        sys.stdout.write(str(next(tree.v, int(inp[1]))).lower() + '\n')
    elif inp[0] == 'prev':
        sys.stdout.write(str(prev(tree.v, int(inp[1]))).lower() + '\n')
    else:
        break