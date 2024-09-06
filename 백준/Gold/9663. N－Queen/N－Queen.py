# problem statement : https://www.acmicpc.net/problem/9663
import sys
input = sys.stdin.readline

def make_queens(x):
    global result
    if x == n:
        result += 1
        return
    for i in range(n):
        row[x] = i
        if is_safe(x):
            make_queens(x+1)
    
def is_safe(x):
    for i in range(x):
        if row[x] == row[i] or abs(row[x]-row[i]) == abs(x-i):
            return False
    return True

n = int(input())
result = 0
row = [0]*n
make_queens(0)
print(result)
