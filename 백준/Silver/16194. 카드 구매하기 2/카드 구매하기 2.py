# problem statement : https://www.acmicpc.net/problem/16194
import sys
input = sys.stdin.readline

n = int(input())
cards = list(map(int, input().split()))

dp = [10000]*(n+1)
dp[0] = 0

for i in range(1, n+1):
    for j in range(1, i+1):
        dp[i] = min(dp[i], dp[i-j]+cards[j-1])

print(dp[n])
