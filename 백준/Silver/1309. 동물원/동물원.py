# problem statement : https://www.acmicpc.net/problem/1309
import sys
input = sys.stdin.readline

n = int(input())

dp = [[0]*32 for _ in range(n+1)]
dp[1] = [1, 1, 1]

for i in range(2, n+1):
    dp[i][0] = (dp[i-1][1] + dp[i-1][2]) % 9901
    dp[i][1] = (dp[i-1][0] + dp[i-1][2]) % 9901
    dp[i][2] = (dp[i-1][0] + dp[i-1][1] + dp[i-1][2]) % 9901

result = (dp[n][0] + dp[n][1] + dp[n][2]) % 9901
print(result)