# problem statement : https://www.acmicpc.net/problem/2343
import sys
input = sys.stdin.readline

n, m = map(int, input().split())
arr = list(map(int, input().split()))

low = max(arr)
high = sum(arr)
result = high

while low <= high:
    mid = (low+high) // 2
    count = 1
    current_sum = 0
    check = True
    for i in range(n):
        if current_sum + arr[i] > mid:
            count += 1
            current_sum = arr[i]
            if count > m:
                check = False
        else:
            current_sum += arr[i]
    if check:
        result = mid
        high = mid - 1
    else:
        low = mid + 1
print(result)