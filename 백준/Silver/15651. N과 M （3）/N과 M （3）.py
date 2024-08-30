# problem statement : https://www.acmicpc.net/problem/15651
import sys
input = sys.stdin.readline

def backtracking(n, m, cs):
    if len(cs) == m:
        print(' '.join(map(str, cs)))
        return
    
    for i in range(1, n+1):
        cs.append(i)
        backtracking(n, m, cs)
        cs.pop()

n, m = map(int, input().split())
cs = []
backtracking(n, m, cs)