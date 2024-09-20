# problem statement : https://www.acmicpc.net/problem/2022
import sys
input = sys.stdin.readline
import math
def get_dist(mid):
    h1 = math.sqrt(x**2-mid**2)
    h2 = math.sqrt(y**2-mid**2)
    return (h1*h2) / (h1+h2)

x, y, c = map(float, input().split())
start, end = 0, min(x, y)
result = 0

while end - start > 0.0001:
    mid = (start+end)/2
    if get_dist(mid) >= c:
        result = mid
        start = mid
    else:
        end = mid
print(f'{result:.3f}')