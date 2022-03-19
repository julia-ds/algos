# You have to answer requests "sum of numbers on the segment".
# Array doesn't change. There're many requests. You should answer on each in (1) time.
# Input
# First line contains four integers: 𝑛, 𝑥, 𝑦 and 𝑎0 — length of the array and numbers which generates array 𝑎: 𝑎𝑖=(𝑥⋅𝑎𝑖−1+𝑦)mod216.
# Next line contains four integers: 𝑚, 𝑧, 𝑡 and 𝑏0 — number of requests and numbers which generates array 𝑏: 𝑏𝑖=(𝑧⋅𝑏𝑖−1+𝑡)mod230.
# Array 𝑐 is generating in the following way: 𝑐𝑖=𝑏𝑖mod𝑛.
# Request number 𝑖 is to find sum on segment from min(𝑐2𝑖,𝑐2𝑖+1) to max(𝑐2𝑖,𝑐2𝑖+1) in the array 𝑎.
# 1≤𝑛≤10**7, 0≤𝑚≤10**7. All other number are from 0 to 216. 𝑡 can also be equal to −1.
# Output
# Output sum of all sums.
# Example
# input
# 3 1 2 3
# 3 1 -1 4
# output
# 23
# Note
# 𝑎={3,5,7},𝑏={4,3,2,1,0,230−1},𝑐={1,0,2,1,0,0},
# Requests = {[0,1],[1,2],[0,0]}, sums = {8,12,3}.

def get_pref_a(n, x, y, a0):
    pref_a = [a0]
    a_prev = a0
    for i in range(1, n):
        ai = (x * a_prev + y) % (2 ** 16)
        pref_a.append(ai + pref_a[i - 1])
        a_prev = ai
    return pref_a


def get_b(m, z, t, b0):
    b = [b0]
    for i in range(1, 2 * m):
        b.append((z * b[i - 1] + t) % (2 ** 30))
    return b


def get_result(b, n, m, pref_a):
    res = 0
    for i in range(m):
        c0 = b[2 * i] % n
        c1 = b[2 * i + 1] % n
        l = min(c0, c1)
        r = max(c0, c1)
        if l == 0:
            res += pref_a[r]
        else:
            res += pref_a[r] - pref_a[l - 1]
    return res


n, x, y, a0 = list(map(int, input().split(' ')))
m, z, t, b0 = list(map(int, input().split(' ')))
pref_a = get_pref_a(n, x, y, a0)
b = get_b(m, z, t, b0)
res = get_result(b, n, m, pref_a)
print(res)