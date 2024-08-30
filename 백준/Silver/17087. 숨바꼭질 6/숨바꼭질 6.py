# problem statement : https://www.acmicpc.net/problem/17087
import sys
input = sys.stdin.readline
from math import gcd
from functools import reduce

n, s = map(int, input().split())
bros = list(map(int, input().split()))
bros.append(s)
if n == 1:
    print(abs(bros[0]-s))
else:
    arr = []
    for i in range(n):
        arr.append(abs(bros[i+1]-bros[i]))

    print(reduce(gcd, arr))