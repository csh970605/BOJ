# problem statement : https://www.acmicpc.net/problem/7568

import sys
input = sys.stdin.readline

n = int(input())
arr = []
result = [0]*n
for i in range(n):
    arr.append([list(map(int, input().split())), i])
for i in range(n):
    rank = 1
    for j in range(n):
        if i != j:
            if arr[i][0][0] < arr[j][0][0] and arr[i][0][1] < arr[j][0][1]:
                rank +=1
    result[arr[i][1]] = rank
print(' '.join(str(x) for x in result))