# Implement a balanced binary search tree.
#
# Input
# The input contains several operations with the tree and their amount does not exceed 105.
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

SEPARATOR = "\n"
UNICODE = "utf-8"


class TreeNode:
    def __init__(self, key):
        self.key = key
        self.left = None
        self.right = None
        self.h = 1


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


def get_balance(v):
    if v is None:
        return 0
    return get_h(v.left) - get_h(v.right)


def fix_h(v):
    return max(get_h(v.left), get_h(v.right)) + 1


def rotate_left(q):
    p = q.right
    q.right = p.left
    p.left = q
    q.h = fix_h(q)
    p.h = fix_h(p)
    return p


def rotate_right(p):
    q = p.left
    p.left = q.right
    q.right = p
    p.h = fix_h(p)
    q.h = fix_h(q)
    return q


def balance(v):
    v.h = fix_h(v)
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


avl = None
result = []
stdin = sys.stdin.readlines()
for inp in stdin:
    inp = inp.split(' ')
    if inp[0] == 'insert':
        avl = insert(avl, int(inp[1]))
    elif inp[0] == 'delete':
        avl = delete(avl, int(inp[1]))
    elif inp[0] == 'exists':
        result.append(str(exists(avl, int(inp[1]))).lower())
    elif inp[0] == 'next':
        result.append(str(next(avl, int(inp[1]))).lower())
    else:
        result.append(str(prev(avl, int(inp[1]))).lower())

sys.stdout.buffer.write(SEPARATOR.join(result).encode(UNICODE))