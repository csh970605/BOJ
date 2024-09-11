# problem statement : https://www.acmicpc.net/problem/10610
import sys
input=sys.stdin.readline
from itertools import permutations

n = input().strip()
if '0' not in n:
    print(-1)
    exit()
total_sum = sum(map(int, n))
if total_sum % 3 == 0:
    print(''.join(sorted(n, reverse=True)))
else:
    print(-1)