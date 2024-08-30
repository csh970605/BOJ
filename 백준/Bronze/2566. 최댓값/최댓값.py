# problem statement : https://www.acmicpc.net/problem/2566

arr = [[0 for _ in range(9)] for _ in range(9)]
for i in range(9):
    a = list(map(int, input().split()))
    arr[i] = a
index = []
max = -1
for i in range(9):
    for j in range(9):
        if max <= arr[i][j]:
            max = arr[i][j]
            index = [i+1, j+1]
print(max)
print(index[0], index[1])