# problem statement : https://www.acmicpc.net/problem/15657
import sys
input = sys.stdin.readline

def backtracking(n, m, cs, arr, start):
    if len(cs) == m:
        print(' '.join(map(str, cs)))
        return
    
    for i in range(start, n):
        cs.append(arr[i])
        backtracking(n, m, cs, arr, i)
        cs.pop()

n, m = map(int, input().split())
arr = list(map(int, input().split()))
arr.sort()
cs = []

backtracking(n, m, cs, arr, 0)