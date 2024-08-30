# problem statement : https://www.acmicpc.net/problem/19532

a, b, c, d, e, f = map(int, input().split())
det = a * e - b * d

x = (c * e - b * f) // det
y = (a * f - d * c) // det
print(x, y)