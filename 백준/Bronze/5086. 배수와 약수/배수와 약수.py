# problem statement : https://www.acmicpc.net/problem/5086

while True:
    a, b = list(map(int, input().split()))
    if a == 0 and b == 0:
        break
    if a % b == 0 and a // b > 0:
        print('multiple')
    elif b % a == 0 and b // a > 0:
        print('factor')
    else:
        print('neither')