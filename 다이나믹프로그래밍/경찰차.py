# https://www.acmicpc.net/problem/2618
# 접근 방법
# 1. 사건을 하나씩 탐색하며 경찰차 1과 경찰차 2의 위치와의 거리를 계산하고 거리가 더 작은 것을 기준으로 경찰차를 배치한다.
# 2. 사건이 발생한 거리와 경찰차 1, 경찰차 2와의 거리가 같다면 다음 사건을 확인한다.
# 2-1. 다음 사건의 거리가 이전에 사건이 발생한 거리와의 거리가 다른 경찰차와의 거리보다 짧다면 거기에 출동한 경찰차를 다음 사건이 발생한 지역에 배치한 것으로 가정한다.
# 2-2. 만약 다음 사건의 거리가 이전에 사건이 발생한 거리와의 거리가 다른 경찰차와의 거리보다 멀다면 2번을 확인할 때의 경찰차 거리를 확인해 더 가까운 경찰차를 배치한다.

n = int(input())
w = int(input())
array = [list(map(int, input().split())) for _ in range(w)]
police1 = [1, 1]
police2 = [n, n]

d = [0] * w

distance = 0
for i in range(w):
    x, y = array[i]

    if abs(police1[0] - x) + abs(police1[1] - y) > abs(police2[0] - x) + abs(police2[1] - y):
        d[i] = 2
        distance += abs(police2[0] - x) + abs(police2[1] - y)
        police2 = array[i]
    elif abs(police1[0] - x) + abs(police1[1] - y) < abs(police2[0] - x) + abs(police2[1] - y):
        d[i] = 1
        distance += abs(police1[0] - x) + abs(police1[1] - y)
        police1 = array[i]
    else:
        j = i + 1
        while True:
            x_, y_ = array[j]
            if abs(x - x_) + abs(y - y_) < abs(police1[0] - x_) + abs(police1[1] - y_) and 