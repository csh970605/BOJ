# problem statement : https://www.acmicpc.net/problem/24266

a1, a0 = list(map(int,input().split()))

c = int(input())
n = int(input())



if a1*n + a0 <= c*n and a1 <= c:
    print(1)

else:
    print(0)