# problem statement : https://www.acmicpc.net/problem/11055
import sys
input = sys.stdin.readline

n = int(input())
arr = list(map(int, input().split()))

dp = [0]*n
for i in range(n):
    dp[i] = arr[i]

for i in range(1, n):
    for j in range(i):
        if arr[j] < arr[i]:
            dp[i] = max(dp[i], dp[j]+arr[i])
print(max(dp))