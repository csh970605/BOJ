# problem statement : https://www.acmicpc.net/problem/10798

arr = [input() for _ in range(5)]

result = ''
for i in range(15):
    for j in range(5):
        if i < len(arr[j]):
            result += arr[j][i]

print(result)