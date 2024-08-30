# problem statement : https://www.acmicpc.net/problem/2577

a = int(input())
b = int(input())
c = int(input())

result = str(a*b*c)
arr = [0]*10

for s in result:
    arr[int(s)] += 1

for num in arr:
    print(num)