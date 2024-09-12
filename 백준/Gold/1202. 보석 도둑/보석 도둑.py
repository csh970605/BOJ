# problem statement : https://www.acmicpc.net/problem/1202
import sys
input = sys.stdin.readline
import heapq

n, k = map(int, input().split())
jewelries = []
bags = []
taken = [0] * n
for _ in range(n):
    jewelries.append(list(map(int, input().split())))
for _ in range(k):
    bags.append(int(input()))

bags.sort()
jewelries.sort()
weight = 0
max_heap = []
j = 0
for bag in bags:
    while j < n and jewelries[j][0] <= bag:
        heapq.heappush(max_heap, -jewelries[j][1])
        j += 1
    if max_heap:
        weight += -heapq.heappop(max_heap)
print(weight)