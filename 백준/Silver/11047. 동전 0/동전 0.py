# problem statement : https://www.acmicpc.net/problem/12904
import sys
input = sys.stdin.readline

n, k = map(int, input().split())
coins = []
for _ in range(n):
    coins.append(int(input()))
count = 0
for i in range(len(coins)-1, -1, -1):
    if coins[i] <= k:
        count += k // coins[i]
        k %= coins[i]
print(count)