# problem statement : https://www.acmicpc.net/problem/15658
import sys
input = sys.stdin.readline

def dfs(index, current, plus, minus, multi, div):
    global max_value, min_value

    if index == n:
        max_value = max(max_value, current)
        min_value = min(min_value, current)
        return
    
    if plus:
        dfs(index+1, current+arr[index], plus-1, minus, multi, div)
    if minus:
        dfs(index+1, current-arr[index], plus, minus-1, multi, div)
    if multi:
        dfs(index+1, current*arr[index], plus, minus, multi-1, div)
    if div:
        if current < 0:
            dfs(index+1, -(-current//arr[index]), plus, minus, multi, div-1)
        else:
            dfs(index+1, current//arr[index], plus, minus, multi, div-1)
            


n = int(input())
arr = list(map(int, input().split()))
nums = list(map(int, input().split()))
max_value = -float('inf')
min_value = float('inf')

dfs(1, arr[0], nums[0], nums[1], nums[2], nums[3])

print(max_value)
print(min_value)