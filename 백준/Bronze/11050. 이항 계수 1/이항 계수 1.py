# problem statement : https://www.acmicpc.net/problem/11050

import sys
input = sys.stdin.readline
import math

n, k = list(map(int, input().split()))

print(math.comb(n, k))