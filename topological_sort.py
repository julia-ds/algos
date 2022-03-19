# You are given a directed graph. Find its topological sorting.
# Input
# The first line contains two integers 𝑛 and 𝑚 (1≤𝑛≤100000,𝑚≤100000) — the number of vertices and the number of edges
# in the graph, respectively.
# Next 𝑚 lines describe edges of the graph. Each line contains two integers 𝑣 and 𝑢 (1≤𝑣,𝑢≤𝑛) — describing the edge
# starting at 𝑣 and ending at 𝑢. There can be loops and multiedges.
# Output
# If no topological sorting exists, output "-1".
# Otherwise, output the sequence of vertices which describes the topological ordering. If several orderings exist, output any.
# Example
# input
# 6 6
# 1 2
# 3 2
# 4 2
# 2 5
# 6 5
# 4 6
# output
# 4 6 3 1 2 5

import sys
import threading
from sys import setrecursionlimit


def cycle(adjacency_lst, v, color):
    color[v] = 1
    for u in adjacency_lst[v]:
        if color[u] == 0:
            cycle(adjacency_lst, u, color)
        elif color[u] == 1:
            global found_cycle
            found_cycle = True
            return
    color[v] = 2


def topological_sort(adjacency_lst, v, used, ans):
    used[v] = True
    for u in adjacency_lst[v]:
        if not used[u]:
            topological_sort(adjacency_lst, u, used, ans)
    ans.append(v)


def main():
    n, m = list(map(int, sys.stdin.readline().split(' ')))
    adjacency_lst = [[] for _ in range(n)]
    for i in range(m):
        a, b = list(map(int, sys.stdin.readline().split(' ')))
        a -= 1
        b -= 1
        adjacency_lst[a].append(b)
    color = {i: 0 for i in range(n)}
    global found_cycle
    found_cycle = False
    for v in range(n):
        if color[v] == 0:
            cycle(adjacency_lst, v, color)
            if found_cycle:
                print('-1')
                return

    used = {i: False for i in range(n)}
    ans = []
    for v in range(n):
        if not used[v]:
            topological_sort(adjacency_lst, v, used, ans)
    ans = [e + 1 for e in reversed(ans)]
    print(*ans)


if __name__ == '__main__':
    setrecursionlimit(10 ** 9)
    threading.stack_size(2 ** 26)
    thread = threading.Thread(target=main)
    thread.start()