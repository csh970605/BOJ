# problem statement : https://www.acmicpc.net/problem/2133
import sys
input = sys.stdin.readline

n = int(input())

if n % 2 == 1:
    print(0)
    exit()

dp = [0] * (n + 1)
dp[0] = 1  
dp[2] = 3 

for i in range(4, n + 1, 2):
    dp[i] = dp[i - 2] * 3
    for j in range(4, i + 1, 2):
        dp[i] += dp[i - j] * 2

print(dp[n])