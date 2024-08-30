# problem statement : https://www.acmicpc.net/problem/2798

n, m = list(map(int, input().split()))

arr = sorted(list(map(int, input().split())), reverse=True)
max_value = -1
for i in range(n-2):
    for j in range(i+1, n-1):
        for k in range(j+1, n):
            sum = arr[i] + arr[j] + arr[k]
            if sum >= max_value and sum <= m:
                max_value = sum
print(max_value)