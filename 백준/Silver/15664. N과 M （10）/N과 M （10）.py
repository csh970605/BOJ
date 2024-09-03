# problem statement : https://www.acmicpc.net/problem/15664
import sys
input = sys.stdin.readline

def backtracking(n, m, cs, arr, visited):
    if len(cs) == m:
        result.add(tuple(sorted(cs)))
        return
    
    for i in range(n):
        if not visited[i]:
            visited[i] = 1
            cs.append(arr[i])
            backtracking(n, m, cs, arr, visited)
            cs.pop()
            visited[i] = 0

n, m = map(int, input().split())
arr = list(map(int, input().split()))
cs = []
visited = [0]*(n)
result = set()
backtracking(n, m, cs, arr, visited)
for seq in sorted(result):
    print(' '.join(map(str, seq)))