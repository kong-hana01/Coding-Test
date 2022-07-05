# https://www.acmicpc.net/problem/8979
# 접근 방법
# k 국가의 등수를 반복문을 통해 구한다.
import sys
input = sys.stdin.readline
n, k = map(int, input().split())
rank = [[] for _ in range(n+1)]
for _ in range(n):
    country, gold, silver, bronze = map(int, input().split())
    rank[country]=[gold, silver, bronze]
result = 1
for i in range(1, n+1):
    if rank[i][0] > rank[k][0]:
        result += 1
    elif rank[i][0] == rank[k][0] and rank[i][1] > rank[k][1]:
        result += 1
    elif rank[i][0] == rank[k][0] and rank[i][1] == rank[k][1] and rank[i][2] > rank[k][2]:
        result += 1
print(result)