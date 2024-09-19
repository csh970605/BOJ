# problem statement : https://www.acmicpc.net/problem/11652
import sys
input = sys.stdin.readline
from collections import Counter
n = int(input())
arr = []
for _ in range(n):
    arr.append(int(input()))
count = Counter(arr)
result = min(count.items(), key=lambda x : (-x[1], x[0]))
print(result[0])