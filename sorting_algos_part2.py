import random
import string


MAX_ELEMENT_VALUE = 100


def find_k_stat(arr, k):
    if len(arr) == 1:
        return arr[0]
    pivot_idx = random.randint(0, len(arr) - 1)
    pivot_value = arr[pivot_idx]
    arr[pivot_idx], arr[-1] = arr[-1], arr[pivot_idx]
    i = -1
    for e in range(0, len(arr)):
        if arr[e] < pivot_value:
            arr[e], arr[i + 1] = arr[i + 1], arr[e]
            i += 1
    arr[i + 1], arr[-1] = arr[-1], arr[i + 1]
    pivot_idx = i + 1
    if pivot_idx == k - 1:
        return arr[pivot_idx]
    elif k > pivot_idx:
        return find_k_stat(arr[pivot_idx + 1:], k - pivot_idx - 1)
    else:
        return find_k_stat(arr[:pivot_idx], k)

arr_lenght = int(input())
arr = list(map(int, input().split(' ')))
request_num = int(input())

request_arr = []

for i in range(request_num):
    request_arr.append(list(map(int, input().split(' '))))

for request in request_arr:
    left = request[0]
    right = request[1]
    k = request[2]
    print(find_k_stat(arr[left - 1: right], k))


# You are given an array of integers. Your task is to sort them in non-decreasing order again. But now use counting sort!
# Input
# The sole line contains the elements of the array ai separated by space (0 ≤ ai ≤ 100).
# Output
# Print sorted array.
# Example
# input
# 7 3 4 2 5
# output
# 2 3 4 5 7

def counting_sort(arr):
    cnt = [0 for e in range(0, MAX_ELEMENT_VALUE + 1)]
    for a in arr:
        cnt[a] += 1
    i = 0
    for a in range(0, MAX_ELEMENT_VALUE + 1):
        for c in range(cnt[a]):
            arr[i] = a
            i += 1
    return arr

arr = list(map(int, input().split(' ')))
print(*counting_sort(arr))


# Given 𝑛 rows, print their order after 𝑘 digital sorting phases.
# In this task, you need to implement a numeric sort.
# Input
# The first line of the input file contains the number 𝑛 — the number of lines, 𝑚 — their length, and 𝑘 — the number of digital sort phases (1≤𝑛≤1000, 1≤𝑘≤𝑚≤1000). The next 𝑛 lines contain the strings themselves.
# Output
# Output the lines in the order in which they appear after the 𝑘 phases of digital sorting.
# Example
# input
# 3 3 1
# bbb
# aba
# baa
# output
# aba
# baa
# bbb
# input
# 3 3 2
# bbb
# aba
# baa
# output
# baa
# aba
# bbb

def counting_sort(arr, rank, indices):
    cnt = {key: [] for key in list(string.ascii_lowercase)}
    output = []
    for ind in indices:
        if len(arr[ind]) < rank:
            cnt['a'].append(ind)
        else:
            cnt[arr[ind][-rank]].append(ind)
    for value in cnt.values():
        output += value
    return output

def radix_sort(arr, k):
    indices = [i for i in range(len(arr))]
    for rank in range(k):
        indices = counting_sort(arr, rank + 1, indices)
    return indices

rows_num, rows_lenght, k = list(map(int, input().split(' ')))
arr = []

for i in range(rows_num):
    arr.append(input())

result = radix_sort(arr, k)
for ind in result:
    print(arr[ind])
