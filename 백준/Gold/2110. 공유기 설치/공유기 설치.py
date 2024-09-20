# problem statement : https://www.acmicpc.net/problem/2110
import sys
input = sys.stdin.readline

def routers(dist):
    count = 1
    last_install = arr[0]
    for i in range(1, n):
        if arr[i] - last_install >= dist:
            count += 1
            last_install = arr[i]
    return count >= c

n, c = map(int, input().split())
arr = []
for _ in range(n):
    arr.append(int(input()))
arr.sort()

start = 1
end = arr[-1] - arr[0]
result = 0

while start <= end:
    mid = (start+end) // 2
    if routers(mid):
        result = mid
        start = mid + 1
    else:
        end = mid - 1
print(result)