# You have to answer requests "sum of numbers on the segment".
# Array doesn't change. There're many requests. You should answer on each in ๎ป(1) time.
# Input
# First line contains four integers: ๐, ๐ฅ, ๐ฆ and ๐0 โ length of the array and numbers which generates array ๐: ๐๐=(๐ฅโ๐๐โ1+๐ฆ)mod216.
# Next line contains four integers: ๐, ๐ง, ๐ก and ๐0 โ number of requests and numbers which generates array ๐: ๐๐=(๐งโ๐๐โ1+๐ก)mod230.
# Array ๐ is generating in the following way: ๐๐=๐๐mod๐.
# Request number ๐ is to find sum on segment from min(๐2๐,๐2๐+1) to max(๐2๐,๐2๐+1) in the array ๐.
# 1โค๐โค10**7, 0โค๐โค10**7. All other number are from 0 to 216. ๐ก can also be equal to โ1.
# Output
# Output sum of all sums.
# Example
# input
# 3 1 2 3
# 3 1 -1 4
# output
# 23
# Note
# ๐={3,5,7},๐={4,3,2,1,0,230โ1},๐={1,0,2,1,0,0},
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