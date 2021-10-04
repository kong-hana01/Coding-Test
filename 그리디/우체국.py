# https://www.acmicpc.net/problem/2141
# 접근방법 -> 우체국을 세울 마을의 위치가 아닌 그냥 우체국을 설치할 위치
# 0. 주어진 우체국에 대한 정보를 이중 리스트 형태로 입력받는다.
# 1. 전체 인원수를 더한 인구수에서 각 마을에 있는 인원수를 누적해서 빼고 저장해가며 해당 마을보다 오른쪽 마을에 있는 인구수의 합계를 저장한다. 반대의 경우(왼쪽)도 마찬가지로 한다.
# 2. 한 마을에서 왼쪽에 있는 사람들의 거리를 계산하는 방법은 (이전 마을까지의 누적 인원 수 + 현재 마을까지의 누적 인원 수)이므로 이를 누적해서 더해준다.
# 3. 한 마을에서 오른쪽에 있는 사람들의 거리를 계산하는 방법은 순서를 역으로 바꾼 상태에서의 (이전 마을까지의 누적 인원 수 + 현재 마을까지의 누적 인원 수)이므로 이를 누적해서 더해준다.
# 4. 모든 결과를 누적해서 더한 뒤, 값이 가장 작은 마을을 출력한다.
def calc_dist(town, distance, array, not_reverse):
    if not_reverse:
        town = town[::-1]
        array = array[::-1]
        distance[0] = town[0]
        for i in range(1, n):
            now_pop = town[i] * abs(array[i][0] - array[i-1][0])
            last_pop = distance[i-1] 
            distance[i] = now_pop + last_pop
        return distance[::-1]

    else:
        distance[0] = town[0]
        for i in range(1, n):
            now_pop = town[i] * abs(array[i][0] - array[i-1][0])
            last_pop = distance[i-1] 
            distance[i] = now_pop + last_pop
        return distance


def calc_pop(array, total_population, reverse):
    town = [0 for _ in range(n)]
    if not reverse:
        for i in range(n):
            population = array[i][1]
            total_population -= population
            town[i] = total_population
        
        return town

    else:
        array = array[::-1]
        for i in range(n):
            population = array[i][1]
            total_population -= population
            town[i] = total_population
        
        return town[::-1]

import sys, math
input = sys.stdin.readline
n = int(input())
array = [[] for _ in range(n)]
total_population = 0
for i in range(n):
    x, p =  map(int, input().split())
    array[i] = [x, p, i+1]
    total_population += p

array.sort(key=lambda x: x[0])
distance = [0 for _ in range(n)]
town = calc_pop(array, total_population, False)
dist = calc_dist(town, distance, array, True)
town = calc_pop(array, total_population, True)
dist_r = calc_dist(town, distance, array, False)

min_value = math.inf
result = -1
for i in range(n):
    if min_value > dist[i] + dist_r[i]:
        min_value = dist[i] + dist_r[i]
        result = array[i][2]
print(result)