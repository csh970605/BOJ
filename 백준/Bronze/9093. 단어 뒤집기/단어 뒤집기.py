# problem statement : https://www.acmicpc.net/problem/9093
import sys
input = sys.stdin.readline

n = int(input())

for _ in range(n):
    words = list(map(str, input().split()))
    print(' '.join(word[::-1] for word in words))