# problem statement : https://www.acmicpc.net/problem/25206

grade_dic = {
    'A+' : 4.5,
    'A0' : 4.0,
    'B+' : 3.5,
    'B0' : 3.0,
    'C+' : 2.5,
    'C0' : 2.0,
    'D+' : 1.5,
    'D0' : 1.0,
    'F' : 0.0
}

rate_sum = 0.0
grade_sum = 0.0
for _ in range(20):
    name, rate, grade = input().split()
    rate = float(rate)
    if grade == 'P':
        continue
    else:
        rate_sum += rate
        grade_sum += grade_dic[grade]*rate

print(grade_sum/rate_sum)
