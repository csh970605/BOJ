# problem statement : https://www.acmicpc.net/problem/1427

arr = list(map(int, input()))
arr.sort(reverse=True)
for n in arr:
    print(n, end='')