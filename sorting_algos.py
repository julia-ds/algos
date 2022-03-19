# You are given a small array of integers. Your task is to sort it in non-decreasing order.
# Input
# The first line of the input contains one integer n (1≤n≤1000) — the number of elements in the array. The second line
# contains n integers which do not exceed 109 by absolute value.
# Output
# The sole line of the output should contain the same array but in the non-decreasing order. The elements should be
# separated by space.
# Example
# input
# 10
# 1 8 2 1 4 7 3 2 3 6
# output
# 1 1 2 2 3 3 4 6 7 8

elements_num = int(input())
arr = list(map(int, input().split(' ')[:elements_num]))

for i in range(1, len(arr)):
    value = arr[i]
    j = i - 1
    while j >= 0 and value < arr[j]:
        arr[j + 1] = arr[j]
        j -= 1
    arr[j + 1] = value

print(*arr)


# You are given an array of integers. Your task is to sort them in non-decreasing order.
# Input
# The first line of the input contains one integer n (1≤n≤100000) — the number of elements in the array.
# The second line contains n integers which do not exceed 109 by absolute value.
# Output
# The sole line of the output should contain the same array but in the non-decreasing order.
# The elements should be separated by space.
# Example
# input
# 10
# 1 8 2 1 4 7 3 2 3 6
# output
# 1 1 2 2 3 3 4 6 7 8

def merge_sort(left, right):
    sorted_arr = []
    i = 0
    j = 0
    while i + j < len(left) + len(right):
        if j == len(right) or (i < len(left) and left[i] < right[j]):
            sorted_arr.append(left[i])
            i += 1
        else:
            sorted_arr.append(right[j])
            j += 1
    return sorted_arr

def divide(arr):
    if len(arr) == 1:
        return arr
    else:
        n = int(len(arr) / 2)
        l = arr[:n]
        r = arr[n:]
        left = divide(l)
        right = divide(r)
    return merge_sort(left, right)

elements_num = int(input())
arr = list(map(int, input().split(' ')[:elements_num]))

print(*divide(arr))


# Given an array 𝐴=⟨𝑎1,𝑎2,…,𝑎𝑛⟩ of distinct integers.
# You have to find the number of pairs of indices (𝑖,𝑗) such that 𝑖<𝑗 and 𝑎𝑖>𝑎𝑗.
# Input
# The first line of the input contains integer 𝑛 (1≤𝑛≤500000) — number of elements in array 𝐴.
# The second line contains the elements of the array 𝑎𝑖 (0≤𝑎𝑖≤106) separated by space. No two elements of the array coincide.
# Output one integer — the number of inversions in the given array.
# Examples
# input
# 4
# 1 2 4 5
# output
# 0
# input
# 4
# 5 4 2 1
# output
# 6

def merge_sort_inversions(arr):
    if len(arr) == 1:
        return arr, 0
    else:
        l = arr[:len(arr) // 2]
        r = arr[len(arr) // 2:]
        l, ainv = merge_sort_inversions(l)
        r, binv = merge_sort_inversions(r)
        sorted_arr = []
        i = 0
        j = 0
        inversions = 0 + ainv + binv
    while i < len(l) and j < len(r):
        if l[i] <= r[j]:
            sorted_arr.append(l[i])
            i += 1
        else:
            sorted_arr.append(r[j])
            j += 1
            inversions += (len(l) - i)
    sorted_arr += l[i:]
    sorted_arr += r[j:]
    return sorted_arr, inversions

elements_num = int(input())
arr = list(map(int, input().split(' ')[:elements_num]))

print(merge_sort_inversions(arr)[1])


# You are given an array of integers. Your task is to sort them in non-decreasing order.
# Input
# The first line of the input contains one integer n (1≤n≤100000) — the number of elements in the array.
# The second line contains n integers which do not exceed 109 by absolute value.
# Output
# The sole line of the output should contain the same array but in the non-decreasing order.
# The elements should be separated by space.
# Example
# input
# 10
# 1 8 2 1 4 7 3 2 3 6
# output
# 1 1 2 2 3 3 4 6 7 8

import random


def quicksort(arr):
    def _quicksort(arr, low, high):
        if len(arr) == 1:
            return arr
        if low < high:
            p = partition(arr, low, high)
            _quicksort(arr, low, p)
            _quicksort(arr, p + 1, high)

    def partition(arr, low, high):
        pivot_idx = random.randint(low, high)
        pivot = arr[pivot_idx]
        while True:
            while arr[low] < pivot:
                low += 1
            while arr[high] > pivot:
                high -= 1
            if low >= high:
                return high
            arr[low], arr[high] = arr[high], arr[low]
            low += 1
            high -= 1

    _quicksort(arr, 0, len(arr) - 1)
    return arr

elements_num = int(input())
arr = list(map(int, input().split(' ')[:elements_num]))
print(*quicksort(arr))


# Input data format
# The first line contains a number n (1 < n < 50) — the number of kings.
# The next n lines contain the names and serial numbers of the kings. In each line first
# the name of the king is written, consisting of no more than 20 Latin letters (the first letter of the name is capital,
# all subsequent lowercase), and then through a space its serial number is written in the form of a Roman
# numbers from 1 to 50.
# Output format
# n lines should contain the names and ordinal numbers of the kings, ordered in the necessary way.

def from_roman(num):
    roman_numerals = {'I': 1, 'V': 5, 'X': 10, 'L': 50}
    arabic = 0
    for i, c in enumerate(num):
        if (i + 1) == len(num) or roman_numerals[c] >= roman_numerals[num[i + 1]]:
            arabic += roman_numerals[c]
        else:
            arabic -= roman_numerals[c]
    return arabic

def to_roman(num):
    num_map = [(50, 'L'), (40, 'XL'), (10, 'X'), (9, 'IX'), (5, 'V'), (4, 'IV'), (1, 'I')]
    roman = []
    while num > 0:
        for i, r in num_map:
            while num >= i:
                roman += r
                num -= i
    return "".join(roman)

def insertion_sort(arr):
    for i in range(1, len(arr)):
        value = arr[i]
        j = i - 1
        while j >= 0 and value < arr[j]:
            arr[j + 1] = arr[j]
            j -= 1
        arr[j + 1] = value
    return arr

elements_num = int(input())
list_of_kings = [str(input()) for i in range(elements_num)]

temp_list = []
for king in list_of_kings:
    temp_list.append([king.split(' ')[0], from_roman(king.split(' ')[1])])

sorted_list = insertion_sort(temp_list)

for king in sorted_list:
    print(king[0] + ' ' + to_roman(int(king[1])))