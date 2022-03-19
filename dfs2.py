# One day Polycarp published a funny picture in a social network making a poll about the color of his handle.
# Many of his friends started reposting Polycarp's joke to their news feed. Some of them reposted the reposts and so on.
# These events are given as a sequence of strings "name1 reposted name2", where name1 is the name of the person who
# reposted the joke, and name2 is the name of the person from whose news feed the joke was reposted. It is guaranteed
# that for each string "name1 reposted name2" user "name1" didn't have the joke in his feed yet, and "name2" already
# had it in his feed by the moment of repost. Polycarp was registered as "Polycarp" and initially the joke was only in
# his feed.
# Polycarp measures the popularity of the joke as the length of the largest repost chain.
# Print the popularity of Polycarp's joke.
# Input
# The first line of the input contains integer n (1≤n≤200) — the number of reposts. Next follow the reposts in the
# order they were made. Each of them is written on a single line and looks as "name1 reposted name2".
# All the names in the input consist of lowercase or uppercase English letters and/or digits and have lengths from 2 to
# 24 characters, inclusive.
# We know that the user names are case-insensitive, that is, two names that only differ in the letter case correspond
# to the same social network user.
# Output
# Print a single integer — the maximum length of a repost chain.
# Examples
# input
# 5
# tourist reposted Polycarp
# Petr reposted Tourist
# WJMZBMR reposted Petr
# sdya reposted wjmzbmr
# vepifanov reposted sdya
# output
# 6
# input
# 6
# Mike reposted Polycarp
# Max reposted Polycarp
# EveryOne reposted Polycarp
# 111 reposted Polycarp
# VkCup reposted Polycarp
# Codeforces reposted Polycarp
# output
# 2
# input
# 1
# SoMeStRaNgEgUe reposted PoLyCaRp
# output
# 2

import sys
import threading
from sys import setrecursionlimit


def dfs(adjacency_lst, v, color, cur, cur_len):
    color[v] = cur
    cur_len += 1
    global max_repost
    max_repost = max(max_repost, cur_len)
    for u in adjacency_lst[v]:
        if color[u] == 0:
            dfs(adjacency_lst, u, color, cur, cur_len)


def main():
    edges = []
    reposts = dict()
    reposts['polycarp'] = 0
    v = 1
    n = int(sys.stdin.readline())
    for _ in range(n):
        name1, name2 = sys.stdin.readline().lower().split(' reposted ')
        if name1.strip() not in reposts:
            reposts[name1.strip()] = v
            v += 1
        elif name2.strip() not in reposts:
            reposts[name2.strip()] = v
            v += 1
        edges.append((reposts[name1.strip()], reposts[name2.strip()]))
    adjacency_lst = [[] for _ in range(len(reposts.keys()))]
    for a, b in edges:
        adjacency_lst[a].append(b)
        adjacency_lst[b].append(a)
    color = {i: 0 for i in range(n + 1)}
    cnt = 0
    global max_repost
    max_repost = 0
    for v in range(n):
        if color[v] == 0:
            cnt += 1
            dfs(adjacency_lst, v, color, cnt, 0)
    print(max_repost)


if __name__ == '__main__':
    setrecursionlimit(10 ** 9)
    threading.stack_size(2 ** 26)  
    thread = threading.Thread(target=main)
    thread.start()