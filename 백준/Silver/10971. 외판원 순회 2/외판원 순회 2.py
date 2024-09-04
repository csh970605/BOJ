# problem statement : https://www.acmicpc.net/problem/10971
import sys
input = sys.stdin.readline
from itertools import permutations
n = int(input())
arr = []
for _ in range(n):
    arr.append(list(map(int, input().split())))
result = float('inf')
for per in permutations(range(1, n)):
    current = 0
    start = 0
    check = True
    for i in range(n-1):
        if arr[start][per[i]] != 0:
            current += arr[start][per[i]]
            start = per[i]
        else:
            check = False
            break
    if check and arr[start][0] != 0:
        current += arr[start][0]
        result = min(result, current)
print(result)