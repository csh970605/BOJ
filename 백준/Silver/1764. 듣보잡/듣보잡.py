# problem statement : https://www.acmicpc.net/problem/10816

n, m = list(map(int, input().split()))
arr = set()
for _ in range(n):
    arr.add(input().strip())
count = 0
arr2 = []
for _ in range(m):
    s = input().strip()
    if s in arr:
        arr2.append(s)
        count += 1
arr2.sort()
print(count)
for s in arr2:
    print(s)