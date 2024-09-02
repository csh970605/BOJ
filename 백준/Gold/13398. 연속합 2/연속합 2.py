# problem statement : https://www.acmicpc.net/problem/13398
import sys
input = sys.stdin.readline

n = int(input())
arr = list(map(int, input().split()))
if n == 1:
    print(arr[0])
    exit()
dp = [0]*n 
dp_remove = [0]*n
dp[0] = arr[0]
dp_remove[0] = -99999999999
max_value = dp[0]
for i in range(1, n):
    dp[i] = max(dp[i-1] + arr[i], arr[i])
    dp_remove[i] = max(dp[i-1], dp_remove[i-1]+arr[i])
    max_value = max(max_value, dp[i], dp_remove[i])

print(max_value)