# problem statement : https://www.acmicpc.net/problem/17299
import sys
input = sys.stdin.readline

n = int(input())
max_pos =1000001 
arr = [0]*max_pos

nums = list(map(int, input().split()))
stack = []
result = [-1]*n
for num in nums:
    arr[num] += 1
for i in range(n):
    while stack and arr[nums[stack[-1]]] < arr[nums[i]]:
        result[stack.pop()] = nums[i]
    stack.append(i)
print(' '.join(map(str, result)))