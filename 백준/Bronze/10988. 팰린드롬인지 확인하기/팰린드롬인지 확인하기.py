# problem statement : https://www.acmicpc.net/problem/10988

s = str(input())
s_reverse = s[::-1]
if s == s_reverse:
    print(1)
else:
    print(0)