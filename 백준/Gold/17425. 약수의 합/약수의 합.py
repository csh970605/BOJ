# problem statement : https://www.acmicpc.net/problem/17425
import sys
input = sys.stdin.readline

max_pos = 1000001
div_sum = [0]*max_pos
total_sum = [0]*max_pos

for i in range(1, max_pos):
    for j in range(i, max_pos, i):
        div_sum[j] += i
    total_sum[i] = total_sum[i-1] + div_sum[i]
    

t = int(input())

for _ in range(t):
    n = int(input())
    # print(total_sum[n])
    sys.stdout.write(str(total_sum[n])+"\n")