# problem statement : https://www.acmicpc.net/problem/2720

case_n = int(input())



for _ in range(case_n):
    output = [0, 0, 0, 0]
    d_in = int(input())
    output[0], out = d_in // 25, d_in % 25
    output[1], out = out // 10, out % 10
    output[2], out = out // 5, out % 5
    output[3] = out 
    print(' '.join(map(str,output)))