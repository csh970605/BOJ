# problem statement : https://www.acmicpc.net/problem/2493
import sys
input = sys.stdin.readline

n = int(input())

arr = list(map(int, input().split()))
result = [0]*n
stack = []

for i in range(n):
    while stack and arr[stack[-1]] < arr[i]:
        stack.pop()
    if stack:
        result[i] = stack[-1] + 1
    stack.append(i)
print(' '.join(list(map(str,result))))