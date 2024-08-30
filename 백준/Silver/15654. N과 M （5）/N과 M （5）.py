# problem statement : https://www.acmicpc.net/problem/15652
import sys
input = sys.stdin.readline



def backtracking(n, m, cs, visited, arr):
    if len(cs) == m:
        print(' '.join(map(str, cs)))
        return
    
    for i in range(n):
        if not visited[i]:
            visited[i] = 1
            cs.append(arr[i])
            backtracking(n, m, cs, visited, arr)
            cs.pop()
            visited[i] = 0

n, m = map(int, input().split())
arr = list(map(int, input().split()))
arr.sort()
cs = []
visited = [0]*(n)

backtracking(n, m, cs, visited, arr)