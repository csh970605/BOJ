# problem statement : https://www.acmicpc.net/problem/9012

n = int(input())

for _ in range(n):
    try:
        ps = input().strip()
        stack = []
        for p in ps:
            if p == '(':
                stack.append('(')
            else:
                stack.pop()
        if len(stack):
            print('NO')
        else:
            print('YES')
    except BaseException as ex:
        print('NO')