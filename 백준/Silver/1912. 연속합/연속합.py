# problem statement : https://www.acmicpc.net/problem/1912
import sys
input = sys.stdin.readline

n = int(input())
arr = list(map(int, input().split()))
max_value = -9999999999999
current = -99999999999
for i in range(n):
    current = max(arr[i], current+arr[i])
    max_value = max(max_value, current)
print(max_value)
