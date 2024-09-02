# problem statement : https://www.acmicpc.net/problem/11054
import sys
input = sys.stdin.readline

n = int(input())

arr = list(map(int, input().split()))

dp1 = [1]*n
for i in range(n):
    for j in range(i):
        if arr[j] < arr[i]:
            dp1[i] = max(dp1[i], dp1[j]+1)
dp2 = [1]*n
for i in range(n-1, -1, -1):
    for j in range(i+1, n):
        if arr[j] < arr[i]:
            dp2[i] = max(dp2[i], dp2[j]+1)
max_value = 0
for i in range(n):
    max_value = max(max_value, dp1[i]+dp2[i]-1)
print(max_value)