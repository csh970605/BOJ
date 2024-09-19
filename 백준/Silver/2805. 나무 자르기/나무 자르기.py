# problem statement : https://www.acmicpc.net/problem/2805
import sys
input = sys.stdin.readline

n, m = map(int, input().split())
arr = list(map(int, input().split()))

start = 0
end = max(arr)

while start <= end:
    mid = (start+end) // 2
    total = 0
    
    for tree in arr:
        if tree > mid:
            total += tree - mid
    
    if total >= m:
        start = mid + 1
    else:
        end = mid - 1

print(end)