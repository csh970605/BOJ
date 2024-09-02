# problem statement : https://www.acmicpc.net/problem/2156
import sys
input = sys.stdin.readline

n = int(input())
if n == 1:
    print(int(input()))
    exit()
dp = [0]*n

arr = []
for _ in range(n):
    arr.append(int(input()))

if n == 2:
    print(arr[0] + arr[1])
    exit()

dp[0] = arr[0]
dp[1] = dp[0] + arr[1]
dp[2] = max(dp[0]+arr[2], arr[1]+arr[2], dp[1])

for i in range(3, n):
    dp[i] = max(dp[i-1], dp[i-2]+arr[i], dp[i-3]+arr[i-1]+arr[i])

print(dp[-1])