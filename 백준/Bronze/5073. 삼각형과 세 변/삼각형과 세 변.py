# problem statement : https://www.acmicpc.net/problem/5073

while True:
    arr = list(map(int, input().split()))
    if arr == [0, 0, 0]:
        break
    max_value = max(arr)
    max_index = arr.index(max_value)
    cp_arr = arr.copy()
    del cp_arr[max_index]
    if max_value >= sum(cp_arr):
        print('Invalid')
    elif arr[0] == arr[1] and arr[1] == arr[2]:
        print('Equilateral')
    elif arr[0] == arr[1] or arr[0] == arr[2] or arr[1] == arr[2]:
        print('Isosceles')
    else:
        print('Scalene')