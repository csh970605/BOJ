# problem statement : https://www.acmicpc.net/problem/10810

basket_num, numbers = list(map(int, input().split()))
baskets = [0]*basket_num
for _ in range(numbers):
    i, j, k = list(map(int, input().split()))
    baskets[i-1:j] = [k]*(j-i+1)

for i in baskets:
    print(i, end=' ')