# problem statement : https://www.acmicpc.net/problem/2580
import sys
input = sys.stdin.readline

def fill_blank(index):
    if index == len(blanks):
        for row in arr:
            print(*row)
        exit()
    x, y = blanks[index]
    for i in range(1, 10):
        if is_true(x, y, i):
            arr[x][y] = i
            fill_blank(index+1)
            arr[x][y] = 0
def is_true(x, y, num):
    for i in range(9):
        if arr[x][i] == num or arr [i][y] == num:
            return False
    nx = (x//3)*3
    ny = (y//3)*3
    for i in range(3):
        for j in range(3):
            if arr[nx+i][ny+j] == num:
                return False
    return True

arr = []
blanks = []
for i in range(9):
    command = list(map(int, input().split()))
    arr.append(command)
    for j in range(9):
        if arr[i][j] == 0:
            blanks.append([i, j])
fill_blank(0)