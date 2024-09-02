# problem statement : https://www.acmicpc.net/problem/1654
import sys
input = sys.stdin.readline

k, n = map(int, input().split())
lan_cables = [int(input()) for _ in range(k)]

left, right = 1, max(lan_cables)
result = 0

while left <= right:
    mid = (left + right) // 2
    count = sum(lan // mid for lan in lan_cables)
    
    if count >= n:
        result = mid
        left = mid + 1
    else:
        right = mid - 1

print(result)