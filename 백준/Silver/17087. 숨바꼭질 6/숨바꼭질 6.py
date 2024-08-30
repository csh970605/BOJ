# problem statement : https://www.acmicpc.net/problem/17087
import sys
input = sys.stdin.readline
from math import gcd
from functools import reduce

n, s = map(int, input().split())
bros = list(map(int, input().split()))
bros.append(s)
arr = []
for i in range(n):
    arr.append(bros[i+1]-bros[i])

print(abs(reduce(gcd, arr)))