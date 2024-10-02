# problem statement : https://www.acmicpc.net/problem/17069
import sys
input = sys.stdin.readline

n = int(input())
arr = []
for _ in range(n):
    arr.append(list(map(int, input().split())))

dp = [[[0]*3 for _ in range(n)] for _ in range(n)]

dp[0][1][0] = 1

for i in range(n):
    for j in range(2, n):
        if arr[i][j] == 1:
            continue
        dp[i][j][0] = dp[i][j-1][0] + dp[i][j-1][2]

        if i > 0 :
            dp[i][j][1] = dp[i-1][j][1] + dp[i-1][j][2]
        
        if i > 0 and arr[i-1][j] == 0 and arr[i][j-1] == 0:
            dp[i][j][2] = dp[i-1][j-1][0] + dp[i-1][j-1][1] + dp[i-1][j-1][2]
print(dp[n-1][n-1][0]+dp[n-1][n-1][1]+dp[n-1][n-1][2])