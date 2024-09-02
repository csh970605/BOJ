# problem statement : https://www.acmicpc.net/problem/1699
import sys
input = sys.stdin.readline
n = int(input())
dp = [999999999999] * (n+1)
dp[0] = 0

for i in range(1, n+1):
    sqrt_i = int(i**0.5)
    for j in range(1, sqrt_i+1):
        dp[i] = min(dp[i], dp[i-j**2]+1)

print(dp[n])