# problem statement : https://www.acmicpc.net/problem/1699
import sys
input = sys.stdin.readline
import math
n = int(input())
dp = [999999999999] * (n + 1)
dp[0] = 0

for i in range(1, n + 1):
    sqrt_i = int(math.sqrt(i))
    for j in range(1, sqrt_i+1):
        square = j * j
        dp[i] = min(dp[i], dp[i-square]+1)

print(dp[n])