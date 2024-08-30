# problem statement : https://www.acmicpc.net/problem/1269

n = input()

a = set(list(map(int, input().split())))
b = set(list(map(int, input().split())))
print(len(a-b)+len(b-a))