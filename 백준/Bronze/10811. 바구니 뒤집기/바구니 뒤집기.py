# problem statement : https://www.acmicpc.net/problem/10811

n, m = list(map(int, input().split()))

baskets = [(i+1) for i in range(n)]
for _ in range(m):
    i, j = list(map(int, input().split()))
    baskets[i-1:j] = baskets[i-1:j][::-1]

print(' '.join(map(str, baskets)))