# problem statement : https://www.acmicpc.net/problem/15652
import sys
input = sys.stdin.readline

def backtracking(n, m, cs, start):
    if len(cs) == m:
        print(' '.join(map(str, cs)))
        return
    
    for i in range(start, n+1):
        cs.append(i)
        backtracking(n, m, cs, i)
        cs.pop()

n, m = map(int, input().split())
cs = []
visited = [0]*(n+1)

backtracking(n, m, cs, 1)