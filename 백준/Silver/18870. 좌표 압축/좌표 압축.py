# problem statement : https://www.acmicpc.net/problem/18870

n = int(input())

arr = list(map(int, input().split()))
sort_arr = sorted(set(arr))

arr_dic = {value: index for index, value in enumerate(sort_arr)}
print(' '.join(map(str, [arr_dic[x] for x in arr])))
