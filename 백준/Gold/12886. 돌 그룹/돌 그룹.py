# problem statement : https://www.acmicpc.net/problem/12886
import sys
input = sys.stdin.readline
from collections import deque
def bfs(a, b, c):
    q = deque()
    q.append((a, b, c))
    while q:
        a, b, c = q.popleft()
        if a == b == c:
            return 1
        if a != b:
            if a < b and (a+a, b-a, c) not in visited:
                q.append((a+a, b-a, c))
                visited.add((a+a, b-a, c))
            elif a > b and (a-b, b+b, c) not in visited:
                q.append((a-b, b+b, c))
                visited.add((a-b, b+b, c))
        if a != c:
            if a < c and (a+a, b, c-a) not in visited:
                q.append((a+a, b, c-a))
                visited.add((a+a, b, c-a))
            elif a > c and (a-c, b, c+c) not in visited:
                q.append((a-c, b, c+c))
                visited.add((a-c, b, c+c))
        if b != c:
            if b < c and (a, b+b, c-b) not in visited:
                q.append((a, b+b, c-b))
                visited.add((a, b+b, c-b))
            elif b > c and (a, b-c, c+c) not in visited:
                q.append((a, b-c, c+c))
                visited.add((a, b-c, c+c))
    return 0
            
a, b, c = map(int, input().split())
visited = set()
print(bfs(a, b, c))