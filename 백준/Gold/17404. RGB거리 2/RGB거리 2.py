# problem statement : https://www.acmicpc.net/problem/17404
import sys
input = sys.stdin.readline

n = int(input())
arr = []

for _ in range(n):
    arr.append(list(map(int, input().split())))
result = 999999999999


for i in range(3):
    dp = [[99999999999]*3 for _ in range(n)]
    dp[0][i] = arr[0][i]
    for j in range(3):
        if j != i:
            dp[0][j] = 9999999999
    for j in range(1, n):
        dp[j][0] = min(dp[j-1][1], dp[j-1][2]) + arr[j][0]
        dp[j][1] = min(dp[j-1][0], dp[j-1][2]) + arr[j][1]
        dp[j][2] = min(dp[j-1][0], dp[j-1][1]) + arr[j][2]
    for j in range(3):
        if i != j:
            result = min(result, dp[n-1][j])
print(result)