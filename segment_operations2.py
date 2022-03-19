# You are given an array consisting of 𝑛 integers. Write a program that answers the queries of the following type:
# find the minimum between 𝑢-th and 𝑣-th element, inclusive.
# Input
# The first line contains three integers: 𝑛, 𝑚 and 𝑎1 (1⩽𝑛⩽10**5; 1⩽𝑚⩽10**7; 0⩽𝑎1<16714589) — the number of integers in
# the given array, the number of queries, and the first element of the given array, respectively.
# The second line contains two integers 𝑢1, and 𝑣1 (1⩽𝑢1,𝑣1⩽𝑛) — the first query.
# For the sake of the input size, the array and the queries should be generated.
# The array elements 𝑎2,𝑎3,…,𝑎𝑛 are generated with the following formula:
# 𝑎𝑖+1=(23⋅𝑎𝑖+21563)mod16714589.
# For instance, if 𝑛=10, 𝑎1=12345 the following array should be generated: 𝑎 = (12345, 305498, 7048017, 11694653,
# 1565158, 2591019, 9471233, 570265, 13137658, 1325095).
# The queries are generated in the following way:
# 𝑢𝑖+1=((17⋅𝑢𝑖+751+𝑟𝑖+2𝑖)mod𝑛)+1, 𝑣𝑖+1=((13⋅𝑣𝑖+593+𝑟𝑖+5𝑖)mod𝑛)+1,
# where 𝑟𝑖 — the answer for query 𝑖.
# Be careful, 𝑢𝑖 can be greater than 𝑣𝑖.
# Output
# Print three integers 𝑢𝑚, 𝑣𝑚 and 𝑟𝑚 (the last query, and the answer to it).
# Examples
# input
# 10 8 12345
# 3 9
# output
# 5 3 1565158

def create_array(n, a0):
    arr = [a0]
    a_prev = a0
    for i in range(1, n):
        ai = (23 * a_prev + 21563) % 16714589
        arr.append(ai)
        a_prev = ai
    return arr


def create_sparse_table(arr, n):
    st = []
    i = 0
    while i < n:
        j = 1
        st.append([arr[i]])
        while 1 << j < n:
            st[i].append(None)
            j += 1
        i += 1
    j = 1
    while (1 << j) <= n:
        i = 0
        while (i + (1 << j) - 1) < n:
            st[i][j] = min(st[i][j - 1], st[i + (1 << (j - 1))][j - 1])
            i += 1
        j += 1
    return st


def find_k(n):
    k = [0]
    for i in range(1, n + 1):
        k.append(k[i - 1])
        if 1 << k[i] <= i:
            k[i] += 1
    return k


def find_min(l, r, st, arr, k):
    if l == r:
        return arr[l]
    j = k[r - l] - 1
    return min(st[l][j], st[r - (1 << j) + 1][j])


def create_u(u_prev, answer_prev, i, n):
    return ((17 * u_prev + 751 + answer_prev + 2 * i) % n) + 1


def create_v(v_prev, answer_prev, i, n):
    return ((13 * v_prev + 593 + answer_prev + 5 * i) % n) + 1


n, m, a0 = list(map(int, input().split(' ')))
u, v = list(map(int, input().split(' ')))
k = find_k(n)
arr = create_array(n, a0)
st = create_sparse_table(arr, n)

for i in range(1, m + 1):
    answer = find_min(min(u, v) - 1, max(u, v) - 1, st, arr, k)
    if i < m:
        u = create_u(u, answer, i, n)
        v = create_v(v, answer, i, n)
    else:
        print(str(u) + " ")
        print(str(v) + " ")
        print(str(answer))