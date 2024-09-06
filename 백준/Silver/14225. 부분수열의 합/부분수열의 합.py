# problem statement : https://www.acmicpc.net/problem/14225
import sys
input = sys.stdin.readline
from itertools import combinations

n = int(input())
nums = list(map(int, input().split()))
result = [0] * (sum(nums)+2)
for i in range(1, n+1):
    num_combintations = combinations(nums, i)
    for comb in num_combintations:
        result[sum(comb)] = 1
for i in range(1, len(result)):
    if result[i] == 0:
        print(i)
        break