# problem statement : https://www.acmicpc.net/problem/10815

n = input()

involve_arr = set(list(map(int, input().split())))

m = input()

given_arr = list(map(int, input().split()))

for i in range(len(given_arr)):
    if given_arr[i] in involve_arr:
        given_arr[i] = 1
    else:
        given_arr[i] = 0

print(' '.join(map(str, given_arr)))