# problem statement : https://www.acmicpc.net/problem/2738

n, m = list(map(int, input().split()))
arr1 = [[0 for _ in range(m)] for _ in range(n)]
arr2 = [[0 for _ in range(m)] for _ in range(n)]

for i in range(n):
    a = list(map(int, input().split()))
    for j in range(m):
        arr1[i][j] = a[j]

for i in range(n):
    a = list(map(int, input().split()))
    for j in range(m):
        arr2[i][j] = a[j]

for i in range(n):
    for j in range(m):
        print(arr1[i][j]+arr2[i][j], end=' ')
    print()