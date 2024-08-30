# problem statement : https://www.acmicpc.net/problem/15655
import sys
input = sys.stdin.readline



def backtracking(n, m, cs, visited, arr, start):
    if len(cs) == m:
        print(' '.join(map(str, cs)))
        return
    
    for i in range(start, n):
        if not visited[i]:
            visited[i] = 1
            cs.append(arr[i])
            backtracking(n, m, cs, visited, arr, i+1)
            cs.pop()
            visited[i] = 0

n, m = map(int, input().split())
arr = list(map(int, input().split()))
arr.sort()
cs = []
visited = [0]*(n)

backtracking(n, m, cs, visited, arr, 0)