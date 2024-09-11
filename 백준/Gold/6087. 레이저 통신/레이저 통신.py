# problem statement : https://www.acmicpc.net/problem/6087
import sys
input=sys.stdin.readline
from collections import deque

def bfs(W, H, grid, start, end):
    visit = [[0]*W for _ in range(H)] 
    queue = deque()
    min_n = float('inf')  
    
    sy, sx = start
    ey, ex = end
    queue.append((sy, sx, 4, 0)) 
    visit[sy][sx] = 1
    
    while queue:
        y, x, dir, chg = queue.popleft()
        
        if (y, x) == (ey, ex):
            min_n = min(min_n, chg)
            break
        
        for i in dv_dic[dir]:
            a = chg
            dx = x + dv[i][1]
            dy = y + dv[i][0]
            
            if dir != i:
                a += 1
            
            while 0 <= dy < H and 0 <= dx < W and grid[dy][dx] != '*':
                if not visit[dy][dx]: 
                    visit[dy][dx] = a
                    queue.append((dy, dx, i, a))
                
                dy += dv[i][0]
                dx += dv[i][1]
    
    return min_n - 1 


W, H = map(int, input().split())
grid = [list(input().strip()) for _ in range(H)]

C_pos = []
for y in range(H):
    for x in range(W):
        if grid[y][x] == 'C':
            C_pos.append((y, x))
start, end = C_pos[0], C_pos[1]

dv = [(-1, 0), (1, 0), (0, -1), (0, 1)]
dv_dic = {
    0: (0, 2, 3), 
    1: (1, 2, 3), 
    2: (0, 1, 2),
    3: (0, 1, 3),
    4: (0, 1, 2, 3)
}

result = bfs(W, H, grid, start, end)
print(result)