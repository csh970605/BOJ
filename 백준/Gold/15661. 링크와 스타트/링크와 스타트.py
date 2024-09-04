# problem statement : https://www.acmicpc.net/problem/15661
import sys
input = sys.stdin.readline
from itertools import combinations

def team_ability(team):
    ability = 0
    for i, j in combinations(team, 2):
        ability += arr[i][j] + arr[j][i]
    return ability

def get_min(index, start, link):
    if index == n:
        if len(start) == 0 or len(link) == 0:
            return float('inf')
        start_ability = team_ability(start)
        link_ability = team_ability(link)
        return abs(start_ability - link_ability)

    start.append(index)
    start_diff = get_min(index+1, start, link)
    start.pop()

    link.append(index)
    link_diff = get_min(index+1, start, link)
    link.pop()

    return min(start_diff, link_diff)

n = int(input())
arr = []
for _ in range(n):
    arr.append(list(map(int, input().split())))

print(get_min(0, [], []))