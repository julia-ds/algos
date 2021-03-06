# You are given an array consisting of ð integers. Write a program that answers the queries of the following type:
# find the minimum between ð¢-th and ð£-th element, inclusive.
# Input
# The first line contains three integers: ð, ð and ð1 (1â©½ðâ©½10**5; 1â©½ðâ©½10**7; 0â©½ð1<16714589) â the number of integers in
# the given array, the number of queries, and the first element of the given array, respectively.
# The second line contains two integers ð¢1, and ð£1 (1â©½ð¢1,ð£1â©½ð) â the first query.
# For the sake of the input size, the array and the queries should be generated.
# The array elements ð2,ð3,â¦,ðð are generated with the following formula:
# ðð+1=(23âðð+21563)mod16714589.
# For instance, if ð=10, ð1=12345 the following array should be generated: ð = (12345, 305498, 7048017, 11694653,
# 1565158, 2591019, 9471233, 570265, 13137658, 1325095).
# The queries are generated in the following way:
# ð¢ð+1=((17âð¢ð+751+ðð+2ð)modð)+1, ð£ð+1=((13âð£ð+593+ðð+5ð)modð)+1,
# where ðð â the answer for query ð.
# Be careful, ð¢ð can be greater than ð£ð.
# Output
# Print three integers ð¢ð, ð£ð and ðð (the last query, and the answer to it).
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