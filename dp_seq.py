# Let a1,a2,...,an be a numerical sequence. The length of a sequence is the number of elements in that sequence.
# A sequence ai1,ai2,...,aik is called a subsequence of a sequence a if 1≤i1<i2<...<ik≤n.
# A sequence a is called increasing if a1<a2<...<an.
# You are given a sequence containing n integers. Find its longest increasing subsequence.
# Input data
# The first line contains a single number n (1≤n≤2000) — the length of the subsequence.
# The next line contains n integers ai (-10**9≤ai≤10**9) — elements of the sequence.
# Output
# In the first line print the number k — the length of the largest increasing subsequence.
# In the next line print k numbers — the subsequence itself.
# Examples
# input
# 8
# 1 4 1 5 3 3 4 2
# output
# 3
# 1 4 5
# input
# 3
# 1 2 3
# output
# 3
# 1 2 3

def longest_increasing_subsequence(n, array):
    dp = [[1, None] for _ in range(n)]
    max_len = 1
    max_ind = 0
    for i in range(1, n):
        for j in range(i):
            if (array[j] < array[i]) and dp[j][0] > dp[i][0] - 1:
                dp[i][0] = dp[j][0] + 1
                dp[i][1] = j
        if dp[i][0] > max_len:
            max_len = dp[i][0]
            max_ind = i
    lis = [array[max_ind]]
    next_ind = dp[max_ind][1]
    while next_ind is not None:
        lis = [array[next_ind]] + lis
        next_ind = dp[next_ind][1]
    return max_len, lis


n = int(input())

array = list(map(int, input().split(' ')))
max_len, lis = longest_increasing_subsequence(n, array)
print(max_len)
print(*lis)


# You are given a string. You can perform operations of three types:
# Replace one symbol by another.
# Delete any symbol.
# Insert any symbol in any position of the string.
# The smallest number of operations to be performed in order to transform one string to another one is named edit
# distance or Levenshtein distance.
# Find the Levenshtein distance between two given strings.
# Input
# The input contains two lines that contain two strings. The length of each string does not exceed 1000 symbols and
# they consist of only uppercase Latin letters.
# Output
# The sole line of the output should contain the Levenshtein distance between two given strings.
# Example
# input
# ABCDEFGH
# ACDEXGIH
# output
# 3

def levenshtein(str_1, str_2):
    len1 = len(str_1)
    len2 = len(str_2)
    dp = [[i for i in range(len2 + 1)]] + [[j + 1] + [None for _ in range(len2)] for j in range(len1)]
    for i in range(1, len1 + 1):
        for j in range(1, len2 + 1):
            if str_1[i - 1] == str_2[j - 1]:
                dp[i][j] = dp[i - 1][j - 1]
            else:
                dp[i][j] = min(dp[i - 1][j], dp[i][j - 1], dp[i - 1][j - 1]) + 1
    return dp[len1][len2]


str_1 = input()
str_2 = input()
result = levenshtein(str_1, str_2)
print(result)