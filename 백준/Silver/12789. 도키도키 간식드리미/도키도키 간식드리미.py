# problem statement : https://www.acmicpc.net/problem/12789

n = int(input())
arr = list(map(int, input().split()))
stack = []
now = 0
for num in arr:
    if now+1 == num:
        now = num
    elif stack and now+1 != num:
        try:
            while now+1 == stack[-1]:
                now = stack.pop()
        except IndexError:
            pass
        stack.append(num)
    else:
        stack.append(num)
check = True
while stack:
    num = stack.pop()
    if num != now+1:
        check = False
        break
    now+=1

if check:
    print('Nice')
else:
    print('Sad')