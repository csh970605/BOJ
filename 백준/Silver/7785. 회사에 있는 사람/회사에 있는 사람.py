# problem statement : https://www.acmicpc.net/problem/7785

n = int(input())

arr = set()
for _ in range(n):
    name, state = list(map(str, input().split()))
    if state == 'enter':
        arr.add(name)
    else:
        arr.discard(name)
arr = sorted(arr, reverse=True)
print('\n'.join(map(str, arr)))