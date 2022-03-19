# In an online game, players, as usual, fight monsters and gain experience. In order to fight monsters, they form clans.
# After defeating a monster, all members of the clan that defeated it receive the same number of experience points.
# A feature of this game is that the clans never break up and you cannot leave the clan. The only operation available
# is to unite two clans into one.
# Since there are already a lot of players, you were instructed to write a system for recording the current experience
# of players.
# Input data
# The first line of the input file contains numbers n (1≤n≤200000) and m 1≤m≤200000 — the number of registered players
# and the number of requests.
# The next m lines contain descriptions of queries. Requests are of three types:
# join X Y - join clans that include players X and Y (if they are already in the same clan, then nothing changes).
# add X V - add V points of experience to all members of the clan, which includes player X (1≤V≤100).
# get X - display the current experience of player X.
# Initially, all players have 0 experience and each of them is in a clan consisting of one of them.
# Output
# For each get X request, print the current experience of player X.
# Example
# Input
# 3 6
# add 1 100
# join 1 3
# add 1 50
# get 1
# get 2
# get 3
# Output
# 150
# 0
# 50

import sys
from io import IOBase, BytesIO
from os import read, write, fstat

BUFSIZE = 8192


class FastIO(IOBase):
    newlines = 0

    def __init__(self, file):
        self._fd = file.fileno()
        self.buffer = BytesIO()
        self.writable = "x" in file.mode or "r" not in file.mode
        self.write = self.buffer.write if self.writable else None

    def read(self):
        while True:
            b = read(self._fd, max(fstat(self._fd).st_size, BUFSIZE))
            if not b:
                break
            ptr = self.buffer.tell()
            self.buffer.seek(0, 2), self.buffer.write(b), self.buffer.seek(ptr)
        self.newlines = 0
        return self.buffer.read()

    def readline(self, size: int = ...):
        while self.newlines == 0:
            b = read(self._fd, max(fstat(self._fd).st_size, BUFSIZE))
            self.newlines = b.count(b"\n") + (not b)
            ptr = self.buffer.tell()
            self.buffer.seek(0, 2), self.buffer.write(b), self.buffer.seek(ptr)
        self.newlines -= 1
        return self.buffer.readline()

    def flush(self):
        if self.writable:
            write(self._fd, self.buffer.getvalue())
            self.buffer.truncate(0), self.buffer.seek(0)


class IOWrapper(IOBase):
    def __init__(self, file):
        self.buffer = FastIO(file)
        self.flush = self.buffer.flush
        self.writable = self.buffer.writable
        self.write = lambda s: self.buffer.write(s.encode("ascii"))
        self.read = lambda: self.buffer.read().decode("ascii")
        self.readline = lambda: self.buffer.readline().decode("ascii")


class Disjoint:
    def __init__(self, n):
        self.parent = [i for i in range(n)]
        self.rank = [0] * n
        self.klan = [[i] for i in range(n)]
        self.score = [0 for _ in range(n)]

    def get(self, x):
        if self.parent[x] != x:
            self.parent[x] = self.get(self.parent[x])
        return self.parent[x]

    def join(self, x, y):
        x = self.get(x)
        y = self.get(y)
        if x == y:
            return
        if self.rank[x] > self.rank[y]:
            x, y = y, x
        if self.rank[x] == self.rank[y]:
            self.rank[y] += 1
        self.parent[x] = y
        self.klan[y].extend(self.klan[x])
        self.klan[x] = list()

    def add(self, x, v):
        x = self.get(x)
        for player in self.klan[x]:
            self.score[player] += v


stdin, stdout = IOWrapper(sys.stdin), IOWrapper(sys.stdout)
n, m = list(map(int, stdin.readline().split(" ")))
snm = Disjoint(n)
for _ in range(m):
    inp = stdin.readline().split(" ")
    if inp[0] == "join":
        snm.join(int(inp[1]) - 1, int(inp[2]) - 1)
    elif inp[0] == "add":
        snm.add(int(inp[1]) - 1, int(inp[2]))
    elif inp[0] == "get":
        stdout.write(str(snm.score[int(inp[1]) - 1]) + "\n")