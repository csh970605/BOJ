# problem statement : https://www.acmicpc.net/problem/1149
import sys
input = sys.stdin.readline

t = int(input())
arr = []

for _ in range(t):
    arr.append(list(map(int, input().split())))

dp = [[0]*3 for _ in range(t)]
dp[0][0] = arr[0][0]
dp[0][1] = arr[0][1]
dp[0][2] = arr[0][2]

for i in range(1, t):
    dp[i][0] = min(dp[i-1][1], dp[i-1][2]) + arr[i][0]
    dp[i][1] = min(dp[i-1][0], dp[i-1][2]) + arr[i][1]
    dp[i][2] = min(dp[i-1][0], dp[i-1][1]) + arr[i][2]

print(min(dp[t-1][0], dp[t-1][1], dp[t-1][2]))
    
    
