# The grasshopper is traveling from cell 1 to cell 𝑛. At the beginning, the grasshopper sits on cell 1.
# The cells are numbered from 1 to 𝑛. He can move from 1 to 𝑘 cells forward in one jump.
# In each cell grasshopper can get or lose several gold coins (for each cell this number is known).
# Determine how the grasshopper needs to jump to maximize the total number of coins in the end.
# Consider that the grasshopper cannot jump backwards.
# Input
# The first line contains two integers 𝑛 and 𝑘 (3≤𝑛≤10000, 1≤𝑘≤10000) — the number of cells and the largest jump.
# The second line contains 𝑛−2 integers, the number of coins that the grasshopper gets on each cell, from the second
# to the 𝑛−1-th. If this number is negative, the grasshopper loses coins. All the numbers do not exceed 10000 by
# absolute value.
# Output
# In the first line output the maximal number of coins. In the second line output the number of jumps.
# In the third line output the cells visited by the grasshoper.
# Examples
# input
# 5 3
# 2 -3 5
# output
# 7
# 3
# 1 2 4 5
# input
# 10 3
# -13 -2 -14 -124 -9 -6 -5 -7
# output
# -16
# 4
# 1 3 6 8 10
# input
# 12 5
# -5 -4 -3 -2 -1 1 2 3 4 5
# output
# 14
# 7
# 1 6 7 8 9 10 11 12

def grasshopper(n, k, coins):
    coins = coins + [0]  # для последнего столбика
    dp = [[float('-Inf'), 0] for e in range(n)]
    dp[0][0] = 0
    dp[0][1] = -1
    for i in range(1, n):
        for j in range(1, min(i, k) + 1):
            possible_jump = dp[i - j][0] + coins[i - 1]
            if possible_jump > dp[i][0]:
                dp[i][0] = possible_jump
                dp[i][1] = i - j
    way = [n]
    column = dp[n - 1][1]
    while column >= 0:
        way.append(column + 1)
        column = dp[column][1]
    jumps_cnt = len(way) - 1
    max_coins = dp[n - 1][0]
    return max_coins, jumps_cnt, list(reversed(way))


n, k = list(map(int, input().split(' ')))
coins = list(map(int, input().split(' ')))
max_coins, jumps_cnt, way = grasshopper(n, k, coins)
print(max_coins)
print(jumps_cnt)
print(*way)