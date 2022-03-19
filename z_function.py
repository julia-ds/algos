# Compute Z-function for a given string s.
# Input
# Single line contains string s of only Latin letters (1≤|s|≤10**6).
# Output
# Output values of the Z-function for string s for indices 2,3,...,|s|.
# Examples
# input
# aaaAAA
# output
#  2 1 0 0 0
# input
# abacaba
# output
#  0 1 0 3 0 1

import sys


def z_func(word):
    left = 0
    right = 0
    n = len(word)
    z = [0 for _ in range(n)]
    z[0] = None
    for i in range(1, n):
        z[i] = max(0, min(right - i, z[i - left]))
        while i + z[i] < n and word[z[i]] == word[i + z[i]]:
            z[i] += 1
            if i + z[i] > right:
                left = i
                right = i + z[i]
    return z


def main():
    word = sys.stdin.readline().strip()
    output = [str(a) for a in z_func(word)[1:]]
    sys.stdout.write(' '.join(output))


if __name__ == '__main__':
    main()