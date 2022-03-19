# For a given string s answer m requests to check if substrings s[a..b] and s[c..d] are equal.
# Input
# The first line contains string s (1≤|s|≤10**5).
# The second line contains a single integer m — the number of requests (0≤m≤10**5).
# Each of the next m lines contains four integers — a,b,c,d (1≤a≤b≤|s|,1≤c≤d≤|s|).
# Output
# Output m lines. For each request output "Yes", if corresponding strings are equal, and "No" — otherwise.
# Example
# input
# trololo
# 3
# 1 7 1 7
# 3 5 5 7
# 1 1 1 5
# output
# Yes
# Yes
# No

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


P = 39
M = 1e9 + 7


def get_hash(l, r, hash_lst, powp):
    if l == 0:
        return hash_lst[r]
    return (hash_lst[r] - (hash_lst[l - 1] * powp[r - l + 1]) % M + M) % M


def main():
    stdin, stdout = IOWrapper(sys.stdin), IOWrapper(sys.stdout)
    str_ = stdin.readline().strip()
    n = int(stdin.readline())
    hash_lst = [None] * len(str_)
    powp = [None] * len(str_)
    hash_lst[0] = ord(str_[0])
    powp[0] = 1
    for i in range(1, len(str_)):
        s = ord(str_[i])
        hash_lst[i] = ((hash_lst[i - 1] * P) + s) % M
        powp[i] = (powp[i - 1] * P) % M

    for _ in range(n):
        a, b, c, d = map(int, stdin.readline().split(' '))
        substr_hash1 = get_hash(a - 1, b - 1, hash_lst, powp)
        substr_hash2 = get_hash(c - 1, d - 1, hash_lst, powp)
        if substr_hash1 == substr_hash2:
            stdout.write('Yes' + '\n')
        else:
            stdout.write('No' + '\n')


if __name__ == '__main__':
    main()