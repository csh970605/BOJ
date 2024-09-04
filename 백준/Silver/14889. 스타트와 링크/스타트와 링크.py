# problem statement : https://www.acmicpc.net/problem/14889
import sys
input = sys.stdin.readline
from itertools import combinations

def team_ability(team):
    ability = 0
    for i, j in combinations(team, 2):
        ability += arr[i][j] + arr[j][i]
    return ability

def get_min():
    p = range(n)
    min_diff = float('inf')

    for start in combinations(p, int(n/2)):
        link = [player for player in p if player not in start]
        start_ability = team_ability(start)
        link_ability = team_ability(link)
        diff = abs(start_ability - link_ability)
        min_diff = min(min_diff, diff)
    return min_diff

n = int(input())
arr = []
for _ in range(n):
    arr.append(list(map(int, input().split())))

print(get_min())