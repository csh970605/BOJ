n, m = list(map(int, input().split()))

arr1 = set()
for _ in range(n):
    arr1.add(input().strip())

count = 0
for _ in range(m):
    if input().strip() in arr1:
        count += 1

print(count)