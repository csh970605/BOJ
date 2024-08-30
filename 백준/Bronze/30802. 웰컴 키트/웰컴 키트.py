# problem statement : https://www.acmicpc.net/problem/30802

import sys
input = sys.stdin.readline
import math

n = int(input())

t = list(map(int, input().split()))

tb, pb = list(map(int, input().split()))
tcount = 0
for size in t:
    tcount += math.ceil(size/tb)
print(tcount)
print(n//pb, n%pb)