# problem statement : https://www.acmicpc.net/problem/1891
import sys
input = sys.stdin.readline

def get_co(d, start):
    size = 2 ** d 
    x, y = 0, 0
    start = str(start)

    for co in start:
        size //= 2
        if co == '1':
            x += size
            y += size
        elif co == '2':
            y += size
        elif co == '4': 
            x += size
    
    return x, y

def get_quad(d, x, y):
    quad = ''
    size = 2 ** d
    for _ in range(d):
        size //= 2
        if x >= size and y >= size:
            quad += '1'
            x -= size
            y -= size
        elif x < size and y >= size:
            quad += '2'
            y -= size
        elif x < size and y < size:
            quad += '3'
        elif x >= size and y < size:
            quad += '4'
            x -= size
    return quad

d, start = map(int, input().split())

x, y = get_co(d, start)
dx, dy = map(int, input().split())
nx = x + dx
ny = y + dy
if 0 <= nx < 2**d and 0 <= ny < 2**d:
    print(get_quad(d, nx, ny))
else:
    print(-1)