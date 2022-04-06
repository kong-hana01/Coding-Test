# https://www.acmicpc.net/problem/10655
# 접근 방법
# 체크포인트와의 거리를 모두 더해가며 가장 거리가 먼 경우를 따로 구해 이를 전체 거리에서 뺸 뒤 출력한다.
import sys, math
input = sys.stdin.readline
n = int(input())
totalDist = 0
maxDist = 0
maxDistXY = []
x1, y1 = map(int, input().split())
for i in range(n-2):
    x2, y2 = map(int, input().split())
    dist = abs(x1-x2) + abs(y1-y2)
    totalDist += dist
    if maxDist < dist:
        maxDIst = dist

    
    x1, y1 = x2, y2
print(totalDist - maxDist)