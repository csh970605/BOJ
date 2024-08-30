# problem statement : https://www.acmicpc.net/problem/2485
import math
import functools
import sys

n = int(input())
arr = []
dist = []
for i in range(n):
    arr.append(int(sys.stdin.readline().strip()))
    if len(arr) > 1:
        dist.append(arr[i]-arr[i-1])

dist_gcd = functools.reduce(math.gcd, dist)
first = arr[0]
last = arr[-1]
count = (last - first) // dist_gcd + 1

print(count - len(arr))