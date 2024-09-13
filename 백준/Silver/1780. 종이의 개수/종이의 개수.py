# problem statement : https://www.acmicpc.net/problem/1780
import sys
input = sys.stdin.readline

def check(x, y, n):
    first = arr[x][y]
    
    for i in range(x, x + n):
        for j in range(y, y + n):
            if arr[i][j] != first:
                for k in range(3):
                    for l in range(3):
                        check(x+k*n//3, y+l*n//3, n//3)
                return
    
    result[first] += 1

n = int(input())
arr = []
for _ in range(n):
    arr.append(list(map(int, input().split())))
result = {-1: 0, 0: 0, 1: 0}
check(0, 0, n)
print(result[-1])
print(result[0])
print(result[1])