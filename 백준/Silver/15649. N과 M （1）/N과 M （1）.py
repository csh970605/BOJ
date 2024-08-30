# problem statement : https://www.acmicpc.net/problem/15649
import sys
input = sys.stdin.readline

def backtracking(n, m, visited, cs):
    if len(cs) == m:
        print(' '.join(map(str, cs)))
        return
    
    for i in range(1, n+1):
        if not visited[i]:
            visited[i] = True
            cs.append(i)
            backtracking(n, m, visited, cs)
            cs.pop()
            visited[i]= False

n, m = map(int, input().split())
visited = [0]*(n+1)
cs = []
backtracking(n, m, visited, cs)