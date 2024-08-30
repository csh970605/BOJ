# problem statement : https://www.acmicpc.net/problem/9466
import sys
input = sys.stdin.readline
sys.setrecursionlimit(10**6)

def dfs(student, result):
    visited[student] = 1
    cycle[student] = 1
    next = students[student] - 1
    if not visited[next]:
        result = dfs(next, result)
    elif cycle[next]:
        temp = next
        while temp != student:
            result += 1
            temp = students[temp] - 1
        result += 1
    cycle[student] = 0

    return result



t = int(input())
for _ in range(t):
    n = int(input())
    students = list(map(int, input().split()))
    visited = [0]*n
    cycle = [0]*n
    result = 0

    for i in range(n):
        if not visited[i]:
            result = dfs(i, result)
    print(n-result)

