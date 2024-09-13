# problem statement : https://www.acmicpc.net/problem/1074
import sys
input = sys.stdin.readline

def dfs(n, x, y):
    global count
    if n == 0:
        return

    size = 2 ** (n-1) 
    if r < x+size and c < y+size:
        dfs(n - 1, x, y)
    elif r < x+size and c >= y+size:
        count += size * size
        dfs(n-1, x, y+size)
    elif r >= x+size and c < y+size:
        count += 2 * size * size
        dfs(n-1, x+size, y)
    else:
        count += 3 * size * size
        dfs(n-1, x+size, y+size)

n, r, c = map(int, input().split())
count = 0
dfs(n, 0, 0)
print(count)