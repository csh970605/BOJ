# problem statement : https://www.acmicpc.net/problem/1790
import sys
input = sys.stdin.readline

def digit_length(x):
    length = 0
    digit = 1
    num = 9
    while x > num:
        length += num * digit
        x -= num
        digit += 1
        num *= 10
    length += x * digit
    return length

n, k = map(int, input().split())
left, right = 1, n
result = -1

while left <= right:
    mid = (left + right) // 2
    if digit_length(mid) < k:
        left = mid + 1
    else:
        right = mid - 1
        result = mid

total_length = digit_length(result)

if total_length < k:
    print(-1)
    exit()
index = total_length - k
print(str(result)[-index-1])