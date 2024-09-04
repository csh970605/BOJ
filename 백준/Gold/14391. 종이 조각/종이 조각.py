# problem statement : https://www.acmicpc.net/problem/14391
import sys
input = sys.stdin.readline

n, m = map(int, input().split())
arr = []
for i in range(n):
    row = list(map(int, input().strip()))
    arr.append(row)
result = 0
for mask in range(1 << (n*m)):
    temp = 0
    for i in range(n):
        current = 0
        for j in range(m):
            index = i * m + j
            if mask & (1 << index):
                current = current * 10 + arr[i][j]
            else:
                temp += current
                current = 0
        temp += current
    
    for i in range(m):
        current = 0
        for j in range(n):
            index = j * m + i
            if not mask & (1 << index):
                current = current * 10 + arr[j][i]
            else:
                temp += current
                current = 0
        temp += current
    
    result = max(result, temp)

print(result)
    
