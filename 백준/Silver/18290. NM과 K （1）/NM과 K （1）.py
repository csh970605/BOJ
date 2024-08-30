# problem statement : https://www.acmicpc.net/problem/18290
import sys
input = sys.stdin.readline

def dfs(n, m, k, count, current_sum, x, y, arr, visited, max_sum):
    if count == k:
        max_sum[0] = max(max_sum[0], current_sum)
        return
    
    for i in range(x, n):
        for j in range(y if i == x else 0, m):
            if visited[i][j] == 0:
                if (i > 0 and visited[i-1][j]) or (i < n-1 and visited[i+1][j]) or (j > 0 and visited[i][j-1]) or (j < m-1 and visited[i][j+1]):
                    continue
                
                visited[i][j] = 1
                dfs(n, m, k, count + 1, current_sum + arr[i][j], i, j + 1, arr, visited, max_sum)
                visited[i][j] = 0

max_sum = [-20000]
n, m, k = map(int, input().split())
arr = [list(map(int, input().split())) for _ in range(n)]
visited = [[0] * m for _ in range(n)]

dfs(n, m, k, 0, 0, 0, 0, arr, visited, max_sum)
print(max_sum[0])
