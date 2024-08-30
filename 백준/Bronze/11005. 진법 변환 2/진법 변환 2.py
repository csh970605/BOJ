# problem statement : https://www.acmicpc.net/problem/11005

num, notation = list(map(int, input().split()))

mapper = {10 + (i - ord('A')) : chr(i) for i in range(ord('A'), ord('Z') + 1)}
result = ''
temp = 0
while True:
    temp = num % notation
    num = num //notation
    if temp >= 10:
        temp = mapper[temp]
    result = ''.join([str(temp), result])
    if num <= 0:
        break

print(result)