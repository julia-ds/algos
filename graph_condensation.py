# Find the number of edges in a condensation of a given oriented graph. Note: condensation doesn't have multiedges.
# Input
# The first line of the input file contains two integers 𝑛 and 𝑚  — the number of vertices and the number of edges
# respectively (𝑛≤10000, 𝑚≤100000). Next 𝑚 lines contain edges description, one line describes one edge.
# Edge number 𝑖 is represented by two numbers 𝑏𝑖,𝑒𝑖  — the start and the end of the edge respectively(1 ≤ 𝑏𝑖, 𝑒𝑖 ≤ 𝑛).
# Graph may have multiedges and loops.
# Output
# Print one integer —the number of edges in a condensation of the graph.
# Example
# input
# 4 4
# 2 1
# 3 2
# 2 3
# 4 3
# output
# 2

import sys
import threading
from sys import setrecursionlimit


def dfs(adjacency_lst, v, color, cur):
    color[v] = cur
    for u in adjacency_lst[v]:
        if color[u] == 0:
            dfs(adjacency_lst, u, color, cur)


def topological_sort(adjacency_lst, v, used, ans):
    used[v] = True
    for u in adjacency_lst[v]:
        if not used[u]:
            topological_sort(adjacency_lst, u, used, ans)
    ans.append(v)


def main():
    n, m = list(map(int, sys.stdin.readline().split(' ')))
    adjacency_lst = [[] for _ in range(n)]
    backward_adjacency_lst = [[] for _ in range(n)]
    for i in range(m):
        a, b = list(map(int, sys.stdin.readline().split(' ')))
        a -= 1
        b -= 1
        adjacency_lst[a].append(b)
        backward_adjacency_lst[b].append(a)
    used = {i: False for i in range(n)}
    ans = []
    for v in range(n):
        if not used[v]:
            topological_sort(adjacency_lst, v, used, ans)
    color = {i: 0 for i in range(n)}
    cnt = 0
    for v in ans[::-1]:
        if color[v] == 0:
            cnt += 1
            dfs(backward_adjacency_lst, v, color, cnt)
    result = set()
    for v, edges in enumerate(adjacency_lst):
        for u in edges:
            if color[v] != color[u]:
                result.add((color[v], color[u]))
    print(len(result))


if __name__ == '__main__':
    setrecursionlimit(10 ** 9)
    threading.stack_size(2 ** 26)
    thread = threading.Thread(target=main)
    thread.start()