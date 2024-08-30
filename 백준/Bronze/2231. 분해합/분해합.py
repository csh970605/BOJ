# problem statement : https://www.acmicpc.net/problem/2231

n = int(input())
check = True
for i in range(1, n):
    num = i
    loop_num = i
    while True:
        num += loop_num % 10
        loop_num = loop_num // 10
        if loop_num <= 0:
            break
    num += loop_num
    if num == n:
        check = False
        print(i)
        break

if check:
    print(0)