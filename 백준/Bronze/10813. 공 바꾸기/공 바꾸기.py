# problem statement : https://www.acmicpc.net/problem/10813

basket_num, numbers = list(map(int, input().split()))
baskets = [i for i in range(1, basket_num+1)]

for _ in range(numbers):
    i, j = list(map(int, input().split()))
    temp = baskets[i-1]
    baskets[i-1] = baskets[j-1]
    baskets[j-1] = temp

for i in baskets:
    print(i, end=' ')