# problem statement : https://www.acmicpc.net/problem/11866

n, k = list(map(int, input().split()))
result = []
arr = []
for i in range(1, n+1):
    arr.append(i)
k -= 1
iter = k
while n >= 0:
    a = arr.pop(iter)
    result.append(str(a))
    n -= 1
    iter = iter + k
    if n == 0:
        break
    if iter >= n:
        iter %= n
result = ', '.join(result)
print(f'<{result}>')