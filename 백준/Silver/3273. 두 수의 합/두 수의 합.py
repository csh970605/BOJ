# problem statement : https://www.acmicpc.net/problem/3273
import sys
input = sys.stdin.readline

n = int(input())
nums = list(map(int, input().split()))
target = int(input())
nums.sort()
left, right = 0, n - 1
result = 0

while left < right:
    current = nums[left] + nums[right]
    if current == target:
        result += 1
        left += 1
        right -= 1
    elif current < target:
        left += 1
    else:
        right -= 1

print(result)