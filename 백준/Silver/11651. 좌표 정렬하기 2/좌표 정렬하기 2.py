# problem statement : https://www.acmicpc.net/problem/11651

n = int(input())
arr=[]
for _ in range(n):
    arr.append(list(map(int, input().split()))[::-1])

arr.sort()

for num in arr:
    print(f'{num[1]} {num[0]}')