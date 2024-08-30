# problem statement : https://www.acmicpc.net/problem/1373
import sys
input = sys.stdin.readline

n = input().strip()
n = int(n, 2)
print(oct(n)[2:])