# problem statement : https://www.acmicpc.net/problem/4949

while True:
    ss = input()
    if ss == '.':
        break
    
    stack = []
    check = True
    
    for s in ss:
        if s == '(' or s == '[':
            stack.append(s)
        elif s == ')':
            if not stack or stack[-1] != '(':
                check = False
                break
            stack.pop()
        elif s == ']':
            if not stack or stack[-1] != '[':
                check = False
                break
            stack.pop()
    
    if check and not stack:
        print('yes')
    else:
        print('no')
