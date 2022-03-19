# There is a rectangular field of size 𝑛×𝑚. The turtle wants to move from cell (1,1) to cell (𝑛,𝑚), in one step she can
# move to the next cell down or right. For each passed cell, the turtle gains (or loses) several gold coins (this number is known for each cell).
# Determine what the maximum number of coins Turtle can collect on the way and how she needs to go for it.
# Input
# The first line contains two integers: 𝑛 and 𝑚 (2≤𝑛,𝑚≤1000). Each of the following 𝑛 lines contains 𝑚 numbers 𝑎𝑖𝑗 (|𝑎𝑖𝑗|≤10),
# which indicate the number of coins received by the turtle on each cell. If this number is negative, the turtle loses coins.
# Output
# In the first line, output maximal number of coins that turtle can collect. In the second output the commands to be executed
# by the turtle, without spaces : the letter «R» indicates a step to the right, and the letter «D» a step down.
# Examples
# input
# 3 3
# 0 2 -3
# 2 -5 7
# 1 2 0
# output
# 6
# RRDD
# input
# 4 5
# 4 5 3 2 9
# 4 6 7 5 9
# 5 2 5 -3 -10
# 3 5 2 9 3
# output
# 41
# RDRDDRR

def turtle(n, m, coins_raw):
    dp = [[[None, None, None] for _ in range(m + 1)] for _ in range(n + 1)]
    for i in range(n + 1):
        dp[i][0][0] = float('-Inf')
    for j in range(m + 1):
        dp[0][j][0] = float('-Inf')
    coins = [[float('-Inf')] * (m + 1)]
    for i in range(n):
        coins.append([float('-Inf')] + coins_raw[i])
    dp[0][1][0] = 0
    for i in range(1, n + 1):
        for j in range(1, m + 1):
            if dp[i - 1][j][0] > dp[i][j - 1][0]:
                dp[i][j][0] = dp[i - 1][j][0] + coins[i][j]
                dp[i][j][1] = i - 1
                dp[i][j][2] = j
            else:
                dp[i][j][0] = dp[i][j - 1][0] + coins[i][j]
                dp[i][j][1] = i
                dp[i][j][2] = j - 1
    i = n
    j = m
    best_route = ""
    i_prev = dp[n][m][1]
    j_prev = dp[n][m][2]
    while i_prev is not None:
        if i == i_prev:
            best_route += best_route.join('R')

        else:
            best_route += best_route.join('D')
        i = i_prev
        j = j_prev
        i_prev = dp[i][j][1]
        j_prev = dp[i][j][2]
    max_coins = dp[n][m][0]
    return max_coins, best_route[::-1][1:]


n, m = list(map(int, input().split(' ')))
coins_raw = []
for row in range(n):
    coins_raw.append(list(map(int, input().split(' '))))
max_coins, best_route = turtle(n, m, coins_raw)
print(max_coins)
print(best_route)