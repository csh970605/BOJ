# problem statement : https://www.acmicpc.net/problem/1085

x, y, w, h = list(map(int, input().split()))

l = x - 0
b = y - 0
r = w - x
t = h - y

print(min([l, t, r, b]))