# problem statement : https://www.acmicpc.net/problem/3085
import sys
input = sys.stdin.readline

def check_length():
    MAX = 0
    for i in range(t):
        row = 1
        col = 1
        for j in range(1, t):
            if arr[i][j] == arr[i][j-1]:
                row += 1
            else:
                row = 1
            if arr[j][i] == arr[j-1][i]:
                col += 1
            else:
                col = 1
            MAX = max(MAX, row, col)
    return MAX

t = int(input())
result = 0

arr = []

for _ in range(t):
    arr.append(list(map(str, input().strip())))

for i in range(t):
    for j in range(t):
        if j+1 < t:
            arr[i][j], arr[i][j+1] = arr[i][j+1], arr[i][j]
            result = max(result, check_length())
            arr[i][j], arr[i][j+1] = arr[i][j+1], arr[i][j]
        if i+1 < t:
            arr[i][j], arr[i+1][j] = arr[i+1][j], arr[i][j]
            result = max(result, check_length())
            arr[i][j], arr[i+1][j] = arr[i+1][j], arr[i][j]
print(result)