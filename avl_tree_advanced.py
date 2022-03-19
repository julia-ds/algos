# Write a program that implements a data structure that allows you to add and remove elements, and also find the 𝑘-th maximum.
# Input
# The first line of the input file contains a natural number 𝑛 (1≤𝑛≤100000) — the number of commands.
# Next 𝑛 lines contain one command each. The command is written in the form of two numbers 𝑐𝑖 and 𝑘𝑖 (|𝑘𝑖|≤109) — the
# type and the argument of the command, respectively. Supported Commands:
#  1: Add an item with the key 𝑘𝑖.
#  0: Find and print the 𝑘𝑖-th maximum.
# -1: Delete the item with the key 𝑘𝑖.
# It is guaranteed that the structure is not required to store elements with equal keys or to delete nonexistent elements.
# It is also guaranteed that when requesting the 𝑘𝑖-th maximum, it exists.
# Output
# Output the result of each command of the second type on a separate line.
# Example
# input
# 11
# 1 5
# 1 3
# 1 7
# 0 1
# 0 2
# 0 3
# -1 5
# 1 10
# 0 1
# 0 2
# 0 3
# output
# 7
# 5
# 3
# 10
# 7
# 3

import sys


class TreeNode:
    def __init__(self, key):
        self.key = key
        self.left = None
        self.right = None
        self.h = 1
        self.size = 1


def insert(v, x):
    if v is None:
        return TreeNode(x)
    elif v.key == x:
        return v
    elif x < v.key:
        v.left = insert(v.left, x)
    elif x > v.key:
        v.right = insert(v.right, x)
    return balance(v)


def delete(v, x):
    if v is None:
        return None
    if x < v.key:
        v.left = delete(v.left, x)
    elif x > v.key:
        v.right = delete(v.right, x)
    else:
        q = v.left
        p = v.right
        if p is None:
            return q
        v_min = find_min(p)
        v_min.right = delete_min(p)
        v_min.left = q
        return balance(v_min)
    return balance(v)


def find_min(v):
    while v.left is not None:
        v = v.left
    return v


def delete_min(v):
    if v.left is None:
        return v.right
    v.left = delete_min(v.left)
    return balance(v)


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


def get_h(v):
    if v is None:
        return 0
    else:
        return v.h


def get_size(v):
    if v is None:
        return 0
    else:
        return v.size


def get_balance(v):
    if v is None:
        return 0
    return get_h(v.left) - get_h(v.right)


def fix_h(v):
    return max(get_h(v.left), get_h(v.right)) + 1


def fix_size(v):
    return get_size(v.left) + get_size(v.right) + 1


def rotate_left(q):
    p = q.right
    q.right = p.left
    p.left = q
    q.h = fix_h(q)
    p.h = fix_h(p)
    q.size = fix_size(q)
    p.size = fix_size(p)
    return p


def rotate_right(p):
    q = p.left
    p.left = q.right
    q.right = p
    p.h = fix_h(p)
    q.h = fix_h(q)
    p.size = fix_size(p)
    q.size = fix_size(q)
    return q


def balance(v):
    v.h = fix_h(v)
    v.size = fix_size(v)
    if abs(get_balance(v)) < 2:
        return v
    elif get_balance(v) == 2:
        if get_balance(v.left) == -1:
            v.left = rotate_left(v.left)
        v = rotate_right(v)
    elif get_balance(v) == -2:
        if get_balance(v.right) == 1:
            v.right = rotate_right(v.right)
        v = rotate_left(v)
    return v


def find_max(v):
    while v.right is not None:
        v = v.right
    return v.key


def find_kth_max(v, k):
    if k == 1:
        return find_max(v)
    elif v.right is None:
        return find_kth_max(v.left, k - 1)
    elif v.right.size + 1 == k:
        return v.key
    elif v.right.size >= k:
        return find_kth_max(v.right, k)
    else:
        return find_kth_max(v.left, k - (v.right.size + 1))


avl = None
n = int(sys.stdin.readline())
stdin = sys.stdin.readlines()
for inp in stdin:
    inp = inp.split(' ')
    if int(inp[0]) == 1:
        avl = insert(avl, int(inp[1].strip()))
    elif int(inp[0]) == -1:
        avl = delete(avl, int(inp[1].strip()))
    else:
        sys.stdout.write(str(find_kth_max(avl, int(inp[1].strip()))) + '\n')