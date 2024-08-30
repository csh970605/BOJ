# problem statement : https://www.acmicpc.net/problem/4375
import sys
input = sys.stdin.readline

while True:
    try:
        n = int(input().strip())
        remainder = 0
        length = 0
        
        for i in range(1, 1000001):
            remainder = (remainder * 10 + 1) % n
            length += 1
            if remainder == 0:
                print(length)
                break
    except:
        break