# problem statement : https://www.acmicpc.net/problem/3009

arr = []
for _ in range(3):
    arr.append(list(map(int, input().split())))

x_dic = {}
y_dic = {}
for co in arr:
    x, y = co
    if x not in x_dic.keys():
        x_dic[x] = 1
    else:
        x_dic[x] +=1
    if y not in y_dic.keys():
        y_dic[y] = 1
    else:
        y_dic[y] +=1

print(min(x_dic, key=x_dic.get), min(y_dic, key=y_dic.get))