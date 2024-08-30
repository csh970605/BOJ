# problem statement : https://www.acmicpc.net/problem/10814

n = int(input())
arr=[]
for _ in range(n):
    arr.append(list(input().split()))
arr = list(enumerate(arr))
arr = sorted(arr, key=lambda x: (int(x[1][0]), x[0]))
arr = [x[1] for x in arr]

for s in arr:
    print(f'{s[0]} {s[1]}')