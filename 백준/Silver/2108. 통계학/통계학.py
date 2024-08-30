# problem statement : https://www.acmicpc.net/problem/2108

import sys
input = sys.stdin.readline
def round(n):
    if n >= 0:
        if n - int(n) >= 0.5:
            return int(n) + 1
        else:
            return int(n)
    else:
        if n - int(n) <= -0.5:
            return int(n) - 1
        else:
            return int(n)
arr = []
n = int(input())
for _ in range(n):
    arr.append(int(input()))
arr.sort()
num_range = arr[-1] - arr[0] + 1
count_arr = [0]*num_range
arr_sum = 0
count = 0
max_value = 0
for num in arr:
    count_arr[num-arr[0]] += 1
    arr_sum += num
print(round(arr_sum/len(arr)))
print(arr[int(n/2)])
for i, num in enumerate(count_arr):
    if num > max_value:
        max_value = num
        index = i
        count = 1
    elif num == max_value and count == 1:
        index = i
        count += 1
print(index+arr[0])
print(arr[-1]-arr[0])