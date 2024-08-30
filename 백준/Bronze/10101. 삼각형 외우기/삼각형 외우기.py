# problem statement : https://www.acmicpc.net/problem/9063

a = int(input())
b = int(input())
c = int(input())

if a+b+c != 180:
    print('Error')
elif a==b and b==c:
    print('Equilateral')
elif a==b or a==c or b==c:
    print('Isosceles')
else:
    print('Scalene')