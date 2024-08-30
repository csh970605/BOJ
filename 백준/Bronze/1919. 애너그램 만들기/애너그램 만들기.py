# problem statement : https://www.acmicpc.net/problem/1919
import sys
input = sys.stdin.readline
from collections import Counter

a = list(map(str,input().strip()))
b = list(map(str,input().strip()))

ac = Counter(a)
bc = Counter(b)
common = sum((ac & bc).values())*2
print(len(a)+len(b)-common)