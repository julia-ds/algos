# Your task is to find connected components of a given undirected graph.
# Input
# The first line of the input file contains two integers 𝑛 and 𝑚 (1≤𝑛≤100000, 0≤𝑚≤200000) — the number of vertices and
# edges of the graph.
# The following 𝑚 lines contain the descriptions of edges one per line. Edge number 𝑖 is described by two
# integers 𝑏𝑖, 𝑒𝑖 (1≤𝑏𝑖,𝑒𝑖≤𝑛) — the numbers of its ends. Loops and parallel edges are allowed.
# Output
# In the first line of the output file output an integer 𝑘, the number of connected components in the graph.
# In the second line output 𝑛 numbers 𝑎1,𝑎2,…,𝑎𝑛 from 1 to 𝑘, where 𝑎𝑖 is the identifier of the connected component
# the 𝑖-th vertex belongs to.
# Examples
# input
# 3 1
# 1 2
# output
# 2
# 1 1 2
# input
# 4 2
# 1 3
# 2 4
# output
# 2
# 1 2 1 2

import sys
import threading
from sys import setrecursionlimit


def dfs(adjacency_lst, v, color, cur):
    color[v] = cur
    for u in adjacency_lst[v]:
        if color[u] == 0:
            dfs(adjacency_lst, u, color, cur)


def main():
    n, m = list(map(int, sys.stdin.readline().split(' ')))
    adjacency_lst = [[] for i in range(n)]
    for i in range(m):
        a, b = list(map(int, sys.stdin.readline().split(' ')))
        a -= 1
        b -= 1
        adjacency_lst[a].append(b)
        adjacency_lst[b].append(a)
    color = {i: 0 for i in range(n)}
    cnt = 0
    for v in range(n):
        if color[v] == 0:
            cnt += 1
            dfs(adjacency_lst, v, color, cnt)

    print(max(color.values()))
    print(*color.values())


setrecursionlimit(10 ** 9)
threading.stack_size(2 ** 26)  # лучше использовать именно эту константу
thread = threading.Thread(target=main)
thread.start()