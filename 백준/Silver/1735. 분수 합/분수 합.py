# problem statement : https://www.acmicpc.net/problem/1735
import math
a, b = list(map(int, input().split()))
c, d = list(map(int, input().split()))

ab = math.gcd(a, b)
cd = math.gcd(c, d)
a, b = a//ab, b//ab
c, d = c//cd, d//cd

top = a*d + b*c
bottom = b*d
bt = math.gcd(bottom, top)
print(int(top//bt), int(bottom//bt))