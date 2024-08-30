# problem statement : https://www.acmicpc.net/problem/14500
import sys
input = sys.stdin.readline

def get_tet1(x, y):
    sum_rtn = 0
    if x+4 <= n:
        temp = [arr[i][y] for i in range(x, x+4)]
        sum_rtn = sum(temp)
    return sum_rtn

def get_tet1_90(x, y):
    sum_rtn = 0
    if y+4 <= m:
        temp = [arr[x][i] for i in range(y, y+4)]
        sum_rtn = sum(temp)
    return sum_rtn

def get_tet2(x, y):
    sum_rtn = 0
    if x+2 <= n and y+2 <= m:
        sum_rtn = sum([arr[x][y], arr[x+1][y], arr[x][y+1], arr[x+1][y+1]])
    return sum_rtn

def get_tet3(x, y):
    sum_rtn = 0
    if x+3 <= n and y+2 <= m:
        sum_rtn = sum([arr[x][y], arr[x+1][y], arr[x+2][y], arr[x+2][y+1]])
    return sum_rtn

def get_tet3_90(x, y):
    sum_rtn = 0
    if x+2 <= n and y+3 <= m:
        sum_rtn = sum([arr[x][y], arr[x+1][y], arr[x][y+1], arr[x][y+2]])
    return sum_rtn

def get_tet3_180(x, y):
    sum_rtn = 0
    if x+3 <= n and y-1 >= 0:
        sum_rtn = sum([arr[x][y], arr[x+1][y], arr[x+2][y], arr[x+2][y-1]])
    return sum_rtn

def get_tet3_270(x, y):
    sum_rtn = 0
    if x+2 <= n and y+3 <= m:
        sum_rtn = sum([arr[x][y], arr[x+1][y], arr[x+1][y+1], arr[x+1][y+2]])
    return sum_rtn

def get_tet4(x, y):
    sum_rtn = 0
    if x+2 <= n and 1 <= y <= m-2:
        sum_rtn = sum([arr[x][y], arr[x+1][y], arr[x+1][y-1],arr[x][y+1]])
    return sum_rtn

def get_tet4_90(x, y):
    sum_rtn = 0
    if x+3 <= n and y+2 <= m:
        sum_rtn = sum([arr[x][y], arr[x+1][y], arr[x+1][y+1], arr[x+2][y+1]])
    return sum_rtn

def get_tet4_180(x, y):
    sum_rtn = 0
    if x+2 <= n and y+3 <= m:
        sum_rtn = sum([arr[x][y], arr[x][y+1], arr[x+1][y+1], arr[x+1][y+2]])
    return sum_rtn

def get_tet4_270(x, y):
    sum_rtn = 0
    if x+3 <= n and y >= 1:
        sum_rtn = sum([arr[x][y], arr[x+1][y], arr[x+1][y-1], arr[x+2][y-1]])
    return sum_rtn

def get_tet5(x, y):
    sum_rtn = 0
    if x+2 <= n and y+3 <= m:
        sum_rtn = sum([arr[x][y], arr[x][y+1], arr[x][y+2], arr[x+1][y+1]])
    return sum_rtn


def get_tet5_90(x, y):
    sum_rtn = 0
    if x+3 <=n and y+2 <= m:
        sum_rtn = sum([arr[x][y], arr[x+1][y], arr[x+1][y+1], arr[x+2][y]])
    return sum_rtn


def get_tet5_180(x, y):
    sum_rtn = 0
    if x >= 1 and y+3 <= m:
        sum_rtn = sum([arr[x][y], arr[x][y+1], arr[x][y+2], arr[x-1][y+1]])
    return sum_rtn


def get_tet5_270(x, y):
    sum_rtn = 0
    if x+3 <= n and y >= 1:
        sum_rtn = sum([arr[x][y], arr[x+1][y], arr[x+1][y-1], arr[x+2][y]])
    return sum_rtn

def get_tet6(x, y):
    sum_rtn = 0
    if x+2 <= n and y+3 <= m:
        sum_rtn = sum([arr[x][y], arr[x][y+1], arr[x][y+2], arr[x+1][y+2]])
    return sum_rtn

def get_tet6_90(x, y):
    sum_rtn = 0
    if x+3 <= n and y+2 <= m:
        sum_rtn = sum([arr[x][y], arr[x+1][y], arr[x+2][y], arr[x][y+1]])
    return sum_rtn

def get_tet6_180(x, y):
    sum_rtn = 0
    if x >= 1 and y+3 <= m:
        sum_rtn = sum([arr[x][y], arr[x][y+1], arr[x][y+2], arr[x-1][y+2]])
    return sum_rtn

def get_tet6_270(x, y):
    sum_rtn = 0
    if x+3 <= n and y+2 <= m:
        sum_rtn = sum([arr[x][y], arr[x][y+1], arr[x+1][y+1], arr[x+2][y+1]])
    return sum_rtn

n, m = map(int, input().split())


arr = []

for _ in range(n):
    arr.append(list(map(int, input().split())))
MAX = 0
for i in range(n):
    for j in range(m):
        MAX = max(get_tet1(i, j), get_tet1_90(i, j), get_tet2(i, j), get_tet3(i, j), get_tet3_90(i, j), get_tet3_180(i, j), get_tet3_270(i, j), get_tet4(i, j), get_tet4_90(i, j), get_tet4_180(i, j), get_tet4_270(i, j), get_tet5(i, j), get_tet5_90(i, j), get_tet5_180(i, j), get_tet5_270(i, j), get_tet6(i, j), get_tet6_90(i, j), get_tet6_180(i, j), get_tet6_270(i, j), MAX)
print(MAX)