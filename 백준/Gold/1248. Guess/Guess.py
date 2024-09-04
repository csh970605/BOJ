# problem statement : https://www.acmicpc.net/problem/1248
import sys
input = sys.stdin.readline

def dfs(index):
    if index == n:
        return True
    
    if matrix[index][index] == 0:
        result[index] = 0
        return dfs(index+1)
    
    for i in range(1, 11):
        result[index] = matrix[index][index] * i
        check = True
        total = 0
        for j in range(index, -1, -1):
            total += result[j]
            if total == 0 and matrix[j][index] != 0:
                check = False
            elif total < 0 and matrix[j][index] != -1:
                check = False
            elif total > 0 and matrix[j][index] != 1:
                check = False
        if check and dfs(index+1):
            return True
    
    return False


n = int(input())
operators = input().strip()
matrix = [[0]*n for _ in range(n)]
k = 0
for i in range(n):
    for j in range(i, n):
        if operators[k] == '0':
            matrix[i][j] = 0
        elif operators[k] == '-':
            matrix[i][j] = -1
        else:
            matrix[i][j] = 1
        k += 1

result = [0] * n
dfs(0)
print(' '.join(map(str, result)))