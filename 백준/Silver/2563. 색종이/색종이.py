# problem statement : https://www.acmicpc.net/problem/2563

arr = [[0 for _ in range(100)] for _ in range(100)]
n = int(input())

for _ in range(n):
    b, l = list(map(int, input().split()))
    t, r = b + 10, l + 10
    for i in range(b, t):
        for j in range(l, r):
            arr[i][j] = 1

print(sum(sum(row) for row in arr))