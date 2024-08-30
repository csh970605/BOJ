# problem statement : https://www.acmicpc.net/problem/15649
import sys
input = sys.stdin.readline

def backtracking(n, m, visited, cs, start):
    if len(cs) == m:
        print(' '.join(map(str, cs)))
        return
    
    for i in range(start, n+1):
        cs.append(i)
        backtracking(n, m, visited, cs, i+1)
        cs.pop()

n, m = map(int, input().split())
visited = [0]*(n+1)
cs = []
backtracking(n, m, visited, cs, 1)