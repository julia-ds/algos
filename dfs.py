# Your task is to find connected components of a given undirected graph.
# Input
# The first line of the input file contains two integers π and π (1β€πβ€100000, 0β€πβ€200000) β the number of vertices and
# edges of the graph.
# The following π lines contain the descriptions of edges one per line. Edge number π is described by two
# integers ππ, ππ (1β€ππ,ππβ€π) β the numbers of its ends. Loops and parallel edges are allowed.
# Output
# In the first line of the output file output an integer π, the number of connected components in the graph.
# In the second line output π numbers π1,π2,β¦,ππ from 1 to π, where ππ is the identifier of the connected component
# the π-th vertex belongs to.
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
threading.stack_size(2 ** 26)  # Π»ΡΡΡΠ΅ ΠΈΡΠΏΠΎΠ»ΡΠ·ΠΎΠ²Π°ΡΡ ΠΈΠΌΠ΅Π½Π½ΠΎ ΡΡΡ ΠΊΠΎΠ½ΡΡΠ°Π½ΡΡ
thread = threading.Thread(target=main)
thread.start()