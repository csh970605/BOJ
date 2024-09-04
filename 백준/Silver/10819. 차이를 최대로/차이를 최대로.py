# problem statement : https://www.acmicpc.net/problem/10819
import sys
input = sys.stdin.readline
from itertools import permutations
n = int(input())
arr = list(map(int, input().split()))
arr.sort()
result = 0
for per in permutations(arr):
    current = 0
    for i in range(n-1):
        current += abs(per[i] - per[i+1])
    result = max(result, current)
print(result)