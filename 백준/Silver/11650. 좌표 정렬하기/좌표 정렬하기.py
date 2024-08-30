# problem statement : https://www.acmicpc.net/problem/11650

n = int(input())

arr = []

for _ in range(n):
    arr.append(list(map(int, input().split())))
arr.sort()

for n in arr:
    print(f'{n[0]} {n[1]}')