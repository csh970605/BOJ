# problem statement : https://www.acmicpc.net/problem/28702

import sys
input = sys.stdin.readline
check = True
for i in range(3):
    s = input().strip()
    if s[0] != 'F' and s[0] !='B' and check:
        index = i
        num = int(s)
        check = False
for i in range(index, 3):
    num+=1

if num % 3 == 0 and num % 5 == 0:
    print('FizzBuzz')
elif num % 3 == 0 and num % 5 != 0:
    print('Fizz')
elif num % 3 != 0 and num % 5 == 0:
    print('Buzz')
else:
    print(num)