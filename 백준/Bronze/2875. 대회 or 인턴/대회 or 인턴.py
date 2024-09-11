# problem statement : https://www.acmicpc.net/problem/2875
import sys
input=sys.stdin.readline
from itertools import permutations

n, m, k = map(int, input().split())

teams = min(n//2, m)
remain = n + m - teams * 3
if k > remain:
    teams -= (k-remain+2) // 3
print(teams)