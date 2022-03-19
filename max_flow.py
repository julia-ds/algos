# There is a system of nodes and pipes that are used for water transportation. For each pipe you know the maximum speed
# that water flowing through that pipe can achieve. Water flows through pipes in such a way that for every node (except
# for the source and the sink), the volume of water going into that node is the same as the volume of water going out
# of that node.
# Your task is to find the maximum volume of water that can flow from the source to the sink, and the speed of water
# inside each pipe. Pipes are bidirectional, meaning that water can flow in any direction. There can be more than one
# pipe between each pair of nodes.
# Input
# The first line contains integer N — the number of nodes (2≤N≤100). The source has number 1 and the sink has number N.
# The second line contains integer M (1≤M≤5000) — number of pipes in the system. Next M lines describe pipes.
# Each pipe is describe by three integers Ai, Bi, Ci, where Ai, Bi are the nodes connected by this pipe (), and
# Ci (0≤Ci≤20) — the maximum speed for that pipe.
# Output
# The first line should contain the maximum volume of water that can flow from the source to the sink.
# Examples
# input
# 2
# 2
# 1 2 1
# 2 1 3
# output
# 4

import sys
import threading


def push_flow(cost, v, t, cur_flow, used, flow):
    used[v] = True
    if v == t:
        return cur_flow
    for u, c in enumerate(cost[v]):
        if not used[u] and flow[v][u] < c:
            next_flow = min(cur_flow, c - flow[v][u])
            delta = push_flow(cost, u, t, next_flow, used, flow)
            if delta > 0:
                flow[u][v] -= delta
                flow[v][u] += delta
                return delta
    return 0


def main() -> None:
    n = int(sys.stdin.readline())
    m = int(sys.stdin.readline())
    flow = {i: [0] * n for i in range(n)}
    cost = {i: [0] * n for i in range(n)}
    for _ in range(m):
        a, b, c = list(map(int, sys.stdin.readline().split(" ")))
        a -= 1
        b -= 1
        cost[a][b] += c
        cost[b][a] += c
    ans = 0
    while True:
        used = {i: False for i in range(n)}
        delta = push_flow(cost, 0, n - 1, 20, used, flow)
        if delta > 0:
            ans += delta
        else:
            break
    print(ans)


if __name__ == '__main__':
    sys.setrecursionlimit(10 ** 9)
    threading.stack_size(2 ** 26)
    thread = threading.Thread(target=main)
    thread.start()