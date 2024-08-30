# problem statement : https://www.acmicpc.net/problem/14215

arr = list(map(int, input().split()))

max_value = max(arr)
max_index = arr.index(max_value)
del arr[max_index]
if sum(arr) <= max_value:
    minimum = sum(arr)-1
    arr.append(minimum)
    print(sum(arr))
else:
    arr.append(max_value)
    print(sum(arr))
