# For two strings s and t find all the occurrences of the string s in the string t.
# Input
# First line contains string s, second — t (1≤|s|,|t|≤10**6). Strings consist of english letters.
# Output
# On the first line output number of occurrences of string s in string t. On the second line output all indices where
# string s occurs in the string t in ascending order, indices begin from 1.
# Example
# input
# aba
# abaCaba
# output
# 2
# 1 5

import sys


def p_func(word):
    n = len(word)
    p = [0 for _ in range(n)]
    for i in range(1, n):
        k = p[i - 1]
        while k > 0 and word[i] != word[k]:
            k = p[k - 1]
        if word[i] == word[k]:
            k += 1
        p[i] = k
    return p


def main():
    p = sys.stdin.readline().strip()
    t = sys.stdin.readline().strip()
    p_len = len(p)
    t_len = len(t)
    output = []
    cnt = 0
    p = p_func(p + '#' + t)
    for i in range(t_len):
        if p[p_len + i + 1] == p_len:
            output.append(i - p_len + 2)
            cnt += 1
    sys.stdout.write(str(cnt) + '\n')
    for res in output:
        sys.stdout.write(str(res) + ' ')
    sys.stdout.write('\n')


if __name__ == '__main__':
    main()
