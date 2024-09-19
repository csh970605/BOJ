# problem statement : https://www.acmicpc.net/problem/11664
import sys
input = sys.stdin.readline
import math

ax, ay, az, bx, by, bz, cx, cy, cz = map(int, input().split())
abx, aby, abz = bx - ax, by - ay, bz - az
acx, acy, acz = cx - ax, cy - ay, cz - az

ab_len_squared = abx**2 + aby**2 + abz**2

dot_product = acx * abx + acy * aby + acz * abz
t = dot_product / ab_len_squared

if t < 0.0:
    closest_x, closest_y, closest_z = ax, ay, az
elif t > 1.0:
    closest_x, closest_y, closest_z = bx, by, bz
else:
    closest_x = ax + t * abx
    closest_y = ay + t * aby
    closest_z = az + t * abz

distance = math.sqrt((cx-closest_x)**2 + (cy-closest_y)**2 + (cz-closest_z)**2)

print(f"{distance:.10f}")