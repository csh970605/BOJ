# problem statement : https://www.acmicpc.net/problem/2587

arr = []
for i in range(5):
    arr.append(int(input()))

arr.sort()
print(int(sum(arr)/len(arr)))
print(arr[2])