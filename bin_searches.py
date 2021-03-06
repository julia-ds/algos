import math

# Given two arrays. The first array is sorted in non-descending order, the second array contains queries - integers.
# For each query, print the number from the first array that is closest (that is, with the minimum modulus of the difference)
# to the number in that query. If there are several of them, print the smallest of them.
# Input data
# The first line of the input contains numbers n and k (0<n,kâ¤10**5).
# The second line contains n numbers of the first array, sorted in non-decreasing order, and the third line contains k
# numbers of the second array. Each number in both arrays modulo does not exceed 2 * 10**9 .
# Output
# For each of the k numbers, print on a separate line the number from the first array that is closest to the given one.
# If there are several of them, print the smallest of them.
# Example
# Input
# 5 5
# 1 3 5 7 9
# 2 4 8 1 6
# Output
# 1
# 3
# 7
# 1
# 5

def bin_search(arr, x):
    lower_bound = 0
    upper_bound = len(arr) - 1
    while lower_bound <= upper_bound:
        m = (lower_bound + upper_bound) // 2
        if arr[m] == x:
            return x
        elif x < arr[m]:
            upper_bound = m - 1
        else:
            lower_bound = m + 1
    if lower_bound == 0:
        return arr[lower_bound]
    elif lower_bound == len(arr):
        return arr[lower_bound - 1]
    elif arr[lower_bound] - x < x - arr[lower_bound - 1]:
        return arr[lower_bound]
    else:
        return arr[lower_bound - 1]

num_of_arr = list(map(int, input().split(' ')))
input_arr = list(map(int, input().split(' ')))
request_arr = list(map(int, input().split(' ')))

for x in request_arr:
    print(bin_search(input_arr, x))


# You are given an array of ğ integers ğ1,ğ2,â¦,ğğ.
# Your task is to answer on the queries of the following type: How many items are between ğ and ğ?.
# Input
# The first line of the input contains ğ â the length of the array (1â¤ğâ¤10**5).
# The second line contains ğ integers ğ1,ğ2,â¦,ğğ (â10**9â¤ğğâ¤10**9).
# The third line contains integer ğ â number of queries (1â¤ğâ¤10**5).
# The following ğ lines contain a pair of integers (ğ,ğ) â query, described above (â10**9â¤ğâ¤ğâ¤10**9).
# Output
# The output must consist of ğ integers â responses for the queries.
# Example
# input
# 5
# 10 1 10 3 4
# 4
# 1 10
# 2 9
# 3 4
# 2 2
# outputCopy
# 5 2 2 0

def bound_search(arr, x):
    lower_bound = -1
    upper_bound = len(arr)
    while lower_bound < upper_bound - 1:
        m = (lower_bound + upper_bound) // 2
        if x <= arr[m]:
            upper_bound = m
        else:
            lower_bound = m
    return upper_bound

arr_lenght = int(input())
arr = list(map(int, input().split(' ')))
num_of_requests = int(input())

bound_arr = []

for i in range(num_of_requests):
    bound_arr.append(list(map(int, input().split(' '))))

sorted_arr = sorted(arr)

for i in range(num_of_requests):
    print(bound_search(sorted_arr, bound_arr[i][1] + 1) - bound_search(sorted_arr, bound_arr[i][0]))


# Find ğ¥ such that ğ¥2+âğ¥=ğ¶ with the precision at least 6 digits after the point.
# Input
# The sole line of the input contains one double 1.0â¤ğ¶â¤1010.
# Output
# The sole line of the output should contain the required ğ¥.
# Examples
# input
# 2.0000000000
# output
# 1.0
# input
# 18.0000000000
# output
# 4.0

y = float(input())
l = 0

EPS = 10 ** (-6)
ITN = math.floor(math.log2((y - l) / EPS))

def bin_search(y, l, r):
    for i in range(0, ITN):
        m = (l + r) / 2
        if m ** 2 + m ** 0.5 < y:
            l = m
        else:
            r = m
    return r

print(bin_search(y, l, y))


# There was a flood in the town of Graffiti Walls! During the disaster the wooden bridge across the river was demolished.
# Bipper and his sister Maple were happy to help citizens but that wasn't enough.
# Now is your turn to save this wonderful town! There are n new timbers prepared for you and the bridge has to consist
# of exactly k timbers. You can cut timbers into smaller ones with integer length, but you can't combine them into one,
# because that would not be solid enough.
# Your task is to find maximal width of the bridge.
# Input
# The first line of input contains two integers n and k (1â¤n,kâ¤10001).
# Each of the following n lines contain one integer ai â the length of the i-th timber (1â¤aiâ¤10**8).
# Output
# The output must contain one integer â maximal width of the bridge.
# If there is no way to make a bridge with the given constraints, answer should be 0.
# Example
# input
# 4 11
# 802
# 743
# 457
# 539
# output
# 200

def max_rope_lenght(arr, houses_num):
    l = 0
    r = arr[-1] + 1  # ÑĞ°Ğ¼Ğ°Ñ Ğ´Ğ»Ğ¸Ğ½Ğ½Ğ°Ñ Ğ²ĞµÑĞµĞ²Ğ¾ÑĞºĞ°
    while l < r - 1:
        m = (l + r) // 2
        if m == 0:
            return 0
        ropes_num = 0
        for rope in arr:
            ropes_num += rope // m
        if ropes_num >= houses_num:
            l = m
        else:
            r = m
    return l

initial_ropes_num, houses_num = list(map(int, input().split(' ')))
arr = []
for i in range(initial_ropes_num):
    arr.append(int(input()))
sorted_arr = sorted(arr)

print(max_rope_lenght(sorted_arr, houses_num))


# You have two copy machines and one copy of very important paper. You need to get n more copies of this paper.
# First copy machine copies one new copy for x seconds, second one for y seconds.
# You can use both copy machines at the same time and copy not only original paper, but copy too.
# You need to find minimal time to get n copies
# Input
# The first line contains three integers n, x and y(1â¤nâ¤2Â·10**8, 1â¤x,yâ¤10).
# Output
# Print one number â minimal time in seconds to get n copies.
# Examples
# input
# 4 1 1
# output
# 3
# input
# 5 1 2
# output
# 4

def fastest_copy_maker(n, speed1, speed2):
    if n == 1:
        return min(speed1, speed2)
    l = 0
    r = max(n * speed1, n * speed2)
    while l < r - 1:
        m = (l + r) // 2
        if (m // speed1 + m // speed2) < n - 1:  # Ñ.Ğº. ÑĞ´ĞµĞ»Ğ°ĞµĞ¼ 1 ĞºĞ¾Ğ¿Ğ¸Ñ Ğ½Ğ° Ğ±ÑÑÑÑĞ¾Ğ¼ Ğ¿ÑĞ¸Ğ½ÑĞµÑĞµ Ğ¸ Ğ´Ğ¾Ğ±Ğ°Ğ²Ğ¸Ğ¼ ÑÑĞ¾ Ğ²ÑĞµĞ¼Ñ Ğ² ĞºĞ¾Ğ½ÑĞµ
            l = m
        else:
            r = m
    return r + min(speed1, speed2)

n, speed1, speed2 = list(map(int, input().split(' ')))
print(fastest_copy_maker(n, speed1, speed2))


# Tarzan has just collected orchids for Jane's Birthday and wants to return back as soon as possible.
# But the way back goes across field and the mighty jungle and it's hard to find the optimal path.
# The plan of the nearest area can be represented as a square, where
# â Tarzan's current position is (0,1).
# â Tarzan's house on a tree is at (1,0).
# â the border between field and jungle is a horizontal line ğ¦=ğ (0â©½ğâ©½1).
# â ğ£ğ, ğ£ğ â Tarzan's speed on the field and in the jungle, respectively.
# Moving along the border is either on the field or in the jungle.
# Find the point on the border, where Tarzan has to enter the jungle, to return back as soon as possible.
# Input
# First line contains two positive integers ğ£ğ and ğ£ğ (1â¤ğ£ğ,ğ£ğâ¤105) â speed on the field and in the jungle, respectively.
# Second line contains a single real number ğ (0â¤ğâ¤1) â coordinate on vertical axis of the border between field and jungle.
# Output
# Output a single real number â coordinate on horizontal axis, where Tarzan should enter the jungle, with accuracy no less than 10â4.
# Example
# input
# 5 3
# 0.4
# output
# 0.783310604

def time_of_travel(x, a, speed_valley, speed_forest):
    return math.sqrt(x ** 2 + (1 - a) ** 2) / speed_valley + math.sqrt(a ** 2 + (1 - x) ** 2) / speed_forest

def fastest_way(a, speed_valley, speed_forest):
    l = 0
    r = 1
    eps = 10 ** (-4)
    while r - l >= eps:
        m1 = l + (r - l) / 3
        m2 = r - (r - l) / 3
        time1 = time_of_travel(m1, a, speed_valley, speed_forest)
        time2 = time_of_travel(m2, a, speed_valley, speed_forest)
        if time1 == time2:
            l = m1
            r = m2
        elif time1 > time2:
            l = m1
        else:
            r = m2
    return r

speed_valley, speed_forest = list(map(int, input().split(' ')))
a = float(input())
print(fastest_way(a, speed_valley, speed_forest))