# 제일 오른쪽 도시를 제외한 나머지 도시 중 리터 당 가격이 가장 싼 도시에서부터 가장 오른쪽 도로까지의 거리만큼 기름을 넣고 간다면 해당 도시부터는 가장 싼 값에 갈 수 있는 방법이 된다.
# 마찬가지로 리터당 가격이 두번째로 싼 도시에서 가장 싼 도시까지의 거리만큼 기름을 넣는다면 해당 도시부터 가장 싼 도시까지의 거리만큼은 가장 싼 값에 갈 수 있는 방법이 된다.
# 다음과 같은 방법을 반복한다면 제일 왼쪽 도시에서 제일 오른쪽 도시로 가는 최소비용을 구할 수 있다.

import sys
sys.setrecursionlimit(10**6)

n = int(sys.stdin.readline())
roads = list(map(int, sys.stdin.readline().split()))
cities = list(map(int, sys.stdin.readline().split()))

cost = cities[0]
total_cost = 0
for i in range(n-1):
    if cost > cities[i]:
        cost = cities[i]
    total_cost += cost * roads[i]

print(total_cost)