# problem statement : https://www.acmicpc.net/problem/15664
import sys
input = sys.stdin.readline

def backtracking(n, m, start, cs, arr):
    if len(cs) == m:
        result.append(tuple(cs))
        return
    
    previous = -1
    for i in range(start, n):
        if previous != arr[i]:
            cs.append(arr[i])
            backtracking(n, m, i + 1, cs, arr)
            cs.pop()
            previous = arr[i]

n, m = map(int, input().split())
arr = sorted(map(int, input().split()))
result = []

backtracking(n, m, 0, [], arr)

for seq in result:
    print(' '.join(map(str, seq)))