# problem statement : https://www.acmicpc.net/problem/14002
import sys
input = sys.stdin.readline

n = int(input())
arr = list(map(int, input().split()))
dp = [1] * n
result = [[num] for num in arr]
for i in range(1, n):
    for j in range(i):
        if arr[i] > arr[j]:
            if dp[i] < dp[j] + 1:
                dp[i] = dp[j] + 1
                result[i] = result[j] + [arr[i]]
print(max(dp))
print(' '.join(map(str, result[dp.index(max(dp))])))