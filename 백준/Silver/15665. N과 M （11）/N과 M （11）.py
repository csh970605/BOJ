# problem statement : https://www.acmicpc.net/problem/15665
import sys
input = sys.stdin.readline
def backtracking(n, m, cs, arr):
    if len(cs) == m:
        result.add(tuple(cs))
        return
    
    for i in range(n):
        cs.append(arr[i])
        backtracking(n, m, cs, arr)
        cs.pop()

n, m = map(int, input().split())
arr = sorted(map(int, input().split()))
result = set()
cs = []

backtracking(n, m, cs, arr)
for seq in sorted(result):
    print(' '.join(map(str, seq)))