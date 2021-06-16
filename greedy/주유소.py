# 제일 오른쪽 도시를 제외한 나머지 도시 중 리터 당 가격이 가장 싼 도시에서부터 가장 오른쪽 도로까지의 거리만큼 기름을 넣고 간다면 해당 도시부터는 가장 싼 값에 갈 수 있는 방법이 된다.
# 마찬가지로 리터당 가격이 두번째로 싼 도시에서 가장 싼 도시까지의 거리만큼 기름을 넣는다면 해당 도시부터 가장 싼 도시까지의 거리만큼은 가장 싼 값에 갈 수 있는 방법이 된다.
# 다음과 같은 방법을 반복한다면 제일 왼쪽 도시에서 제일 오른쪽 도시로 가는 최소비용을 구할 수 있다.

import sys
sys.setrecursionlimit(10**6)

# n = int(sys.stdin.readline())
# road = list(map(int, sys.stdin.readline().split()))
# city = list(map(int, sys.stdin.readline().split()))

# # 리스트.index()함수는 해당 값의 인덱스를 출력해준다. 중복된 값이 다른 원소로 존재한다면 앞에 있는 원소를 기준으로 한다.
# def calculate_cost(index=n-1, cost=0):
#     # index : 최소값이 있는 인덱스 (초기값 : 마지막 도시 제외)
#     # cost : 비용
#     if index == 0:
#         return cost
#     min_cost = min(city[:index])
#     index_ = city.index(min_cost)
#     cost += sum(road[index_:index]) * min_cost
#     return calculate_cost(index_, cost)

# print(calculate_cost())
print(ord('a'))