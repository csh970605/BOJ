# problem statement : https://www.acmicpc.net/problem/1436

n = int(input())

min_5k, min_3k = 0, 0
min_bag = 9999999
for i in range(n//5+1):
    for j in range(n//3+1):
        bags = i + j
        if 5*i + 3*j == n and bags <= min_bag:
            min_5k = i
            min_3k = j
            min_bag = bags

if min_5k == 0 and min_3k == 0:
    print(-1)
else:
    print(min_bag)