# problem statement : https://www.acmicpc.net/problem/13397
import sys
input = sys.stdin.readline

n, m = map(int, input().split())
arr = list(map(int, input().split()))

low = 0
high = max(arr) - min(arr)
result = high

while low <= high:
    mid = (low+high) // 2
    check = True
    count = 1
    min_value = arr[0]
    max_value = arr[0]
    for i in range(1, n):
        min_value = min(min_value, arr[i])
        max_value = max(max_value, arr[i])

        if max_value - min_value > mid:
            count += 1
            min_value = arr[i]
            max_value = arr[i]

            if count > m:
                check = False
    
    if check:
        result = mid
        high = mid - 1
    else:
        low = mid + 1

print(result)