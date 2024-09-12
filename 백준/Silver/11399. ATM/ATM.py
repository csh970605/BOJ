# problem statement : https://www.acmicpc.net/problem/11399
import sys
input = sys.stdin.readline

n = int(input())
arr = list(map(int, input().split()))

arr.sort(reverse=True)
count = 0
for i, time in enumerate(arr):
    count += (i+1) * time
print(count)