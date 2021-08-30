# https://www.acmicpc.net/problem/2836
# 접근 방법
# 출발지가 도착지보다 낮은 번호인 경우는 어차피 0부터 m까지 가야하기에 이를 m을 더한 뒤 그 외의 경우의 수는 합계에서 제외한다.
# 도착지를 기준으로 오름차순 정렬했을 때, 출발지가 도착지보다 높은 번호인 경우의 수만 고려하여 길이를 젠다.
# 출발지가 도착지보다 높은 번호이고 다음과 같은 경우가 동일한 직전 택시 정보와 비교했을 때, 이전 택시의 출발지가 도착지보다 높은 번호인 경우 수를 모두 고려한 뒤, 출발지가 가장 높은 곳의 번호와 도착지가 가장 낮은 곳의 번호를 고려해 길이를 계산한다.
# 단, 이전 택시의 출발지가 현재 탐색중인 택시의 도착지보다 낮은 번호라면 둘을 분리하여 거리를 계산한다.
# 따라서 다음과 같은 계산이 나온다.
# 이전 택시와 겹칠 경우 이동해야하는 거리의 최솟값 = 출발지가 가장 높은 곳의 번호와 도착지가 가장 낮은 번호와의 거리 + 도착지 가장 낮은 번호와 m까지와의 거리 
# 이전택시와 겹치지 않을 경우 이동해야하는 거리의 최솟값 = 이전 택시의 출발지 - 이전 택시의 도착지 + 현재 택시의 출발지 - 이전 택시의 도착지 + 현재 택시의 출발지 - 현재 택시의 도착지
import sys
input = sys.stdin.readline
n, m = map(int, input().split())
taxi = [list(map(int, input().split())) for _ in range(n)]
taxi.sort(key = lambda x: x[1])
max_departure = 0
min_destination = m + 1
distance = m
check = False
for departure, destination in taxi:
    if destination < departure:
        if not max_departure:
            max_departure = departure
            min_destination = destination
            check = True
        elif max_departure < destination:
            distance += 2 * (max_departure - min_destination)
            max_departure = departure
            min_destination = destination
        else:
            max_departure = max(max_departure, departure)
            min_destination = min(min_destination, destination)

if check:
    distance += (max_departure - min_destination) * 2
print(distance)         