# problem statement : https://www.acmicpc.net/problem/1182
import sys
input = sys.stdin.readline
from itertools import combinations

n, s = map(int, input().split())
arr = list(map(int, input().split()))
count = 0
for i in range(1, n+1):
    combination = combinations(arr, i)
    for comb in combination:
        if sum(comb) == s:
            count += 1

print(count)