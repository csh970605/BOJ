# problem statement : https://www.acmicpc.net/problem/15666
import sys
input = sys.stdin.readline
def backtracking(n, m, cs, start, arr):
    if len(cs) == m:
        print(' '.join(map(str, cs)))
        return
    
    last = 0
    for i in range(start, n):
        if last != arr[i]:
            cs.append(arr[i])
            backtracking(n, m, cs, i, arr)
            cs.pop()
            last = arr[i]

n, m = map(int, input().split())
arr = sorted(map(int, input().split()))
result = set()
cs = []

backtracking(n, m, cs, 0, arr)
for seq in sorted(result):
    print(' '.join(map(str, seq)))