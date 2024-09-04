# problem statement : https://www.acmicpc.net/problem/14501
import sys
input = sys.stdin.readline

def recursion(d):
    if d >= n:
        return 0
    if visited[d] != 0:
        return visited[d]
    
    t, p = arr[d]
    if d+t <= n:
        income = p + recursion(d+t)
    else:
        income = 0
    
    skip = recursion(d+1)
    visited[d] = max(income, skip)
    return visited[d]

n = int(input())
arr = []
for _ in range(n):
    arr.append(list(map(int, input().split())))
visited = [0]*n

print(recursion(0))