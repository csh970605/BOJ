# problem statement : https://www.acmicpc.net/problem/13300
import sys
input = sys.stdin.readline

n, k = list(map(int, input().split()))
ym1 = [[]]
yf1 = [[]]
ym2 = [[]]
yf2 = [[]]
ym3 = [[]]
yf3 = [[]]
ym4 = [[]]
yf4 = [[]]
ym5 = [[]]
yf5 = [[]]
ym6 = [[]]
yf6 = [[]]
result = 0
for _ in range(n):
    s, y = list(map(int, input().split()))
    if s == 0:
        if y == 1:
            if len(yf1[0]) == 0:
                yf1[0].append(1)
            elif yf1[0][-1] < k:
                yf1[0][-1] +=1
            elif yf1[0][-1] == k:
                yf1[0].append(1)
        elif y == 2:
                if len(yf2[0]) == 0:
                    yf2[0].append(1)

                elif yf2[0][-1] < k:
                    yf2[0][-1] +=1

                elif yf2[0][-1] == k:
                    yf2[0].append(1)

        elif y == 3:
                if len(yf3[0]) == 0:
                    yf3[0].append(1)

                elif yf3[0][-1] < k:
                    yf3[0][-1] +=1

                elif yf3[0][-1] == k:
                    yf3[0].append(1)



        elif y == 4:
                if len(yf4[0]) == 0:
                    yf4[0].append(1)

                elif yf4[0][-1] < k:
                    yf4[0][-1] +=1

                elif yf4[0][-1] == k:
                    yf4[0].append(1)



        elif y == 5:
                if len(yf5[0]) == 0:
                    yf5[0].append(1)

                elif yf5[0][-1] < k:
                    yf5[0][-1] +=1

                elif yf5[0][-1] == k:
                    yf5[0].append(1)



        elif y == 6:
                if len(yf6[0]) == 0:
                    yf6[0].append(1)

                elif yf6[0][-1] < k:
                    yf6[0][-1] +=1

                elif yf6[0][-1] == k:
                    yf6[0].append(1)



    elif s == 1:
        if y == 1:
                if len(ym1[0]) == 0:
                    ym1[0].append(1)

                elif ym1[0][-1] < k:
                    ym1[0][-1] +=1

                elif ym1[0][-1] == k:
                    ym1[0].append(1)



        elif y == 2:
                if len(ym2[0]) == 0:
                    ym2[0].append(1)

                elif ym2[0][-1] < k:
                    ym2[0][-1] +=1

                elif ym2[0][-1] == k:
                    ym2[0].append(1)



        elif y == 3:
                if len(ym3[0]) == 0:
                    ym3[0].append(1)

                elif ym3[0][-1] < k:
                    ym3[0][-1] +=1

                elif ym3[0][-1] == k:
                    ym3[0].append(1)



        elif y == 4:
                if len(ym4[0]) == 0:
                    ym4[0].append(1)

                elif ym4[0][-1] < k:
                    ym4[0][-1] +=1

                elif ym4[0][-1] == k:
                    ym4[0].append(1)



        elif y == 5:
                if len(ym5[0]) == 0:
                    ym5[0].append(1)

                elif ym5[0][-1] < k:
                    ym5[0][-1] +=1

                elif ym5[0][-1] == k:
                    ym5[0].append(1)



        elif y == 6:
                if len(ym6[0]) == 0:
                    ym6[0].append(1)

                elif ym6[0][-1] < k:
                    ym6[0][-1] +=1

                elif ym6[0][-1] == k:
                    ym6[0].append(1)


print(len(ym1[0])+ len(ym2[0])+ len(ym3[0])+ len(ym4[0])+ len(ym5[0])+ len(ym6[0])+ len(yf1[0])+ len(yf2[0])+ len(yf3[0])+ len(yf4[0])+ len(yf5[0])+ len(yf6[0]))