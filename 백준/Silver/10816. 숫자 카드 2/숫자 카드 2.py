# problem statement : https://www.acmicpc.net/problem/10816

n = int(input())

involved_dic = {}
arr = list(map(int, input().split()))

for num in arr:
    if num in involved_dic.keys():
        involved_dic[num] += 1
    else:
        involved_dic[num] = 1

n = int(input())
arr = list(map(int, input().split()))
for num in arr:
    try:
        print(involved_dic[num], end=' ')
    except BaseException:
        print(0, end=' ')