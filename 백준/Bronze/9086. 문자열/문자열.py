# problem statement : https://www.acmicpc.net/problem/9086

n = int(input())

for _ in range(n):
    s = str(input())
    print(s[0]+s[-1])