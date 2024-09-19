# problem statement : https://www.acmicpc.net/problem/1377
import sys
input = sys.stdin.readline

n = int(input())
arr = []
for i in range(n):
    arr.append((int(input()), i))

arr.sort()
max_move = 0
for i in range(n):
    max_move = max(max_move, arr[i][1]-i)

print(max_move+1)