# https://www.acmicpc.net/problem/7662
# 접근 방법
# 딕셔너리를 통해 현재 힙에 포함되어있는 값은 키, 해당 값의 개수는 밸류로 구현한다.
# 이후 우선순위 큐를 최소 힙, 최대 힙을 통해 구현하고, 값이 생기면 두 힙 모두에 저장하고, 딕셔너리에 키와 값을 추가하거나 값을 하나 증가시켜준다.
# 만약 최솟값이나 최대 값을 삭제하는 경우 딕셔너리에 해당 값이 존재하는지 확인하고, 없다면 해당 값을 그냥 빼준 뒤, 다시 최대값 또는 최솟값을 뺀다.
# 딕셔너리에 해당 값이 존재하는 지에 대한 확인은 set을 통해 진행한다.
import sys, heapq, math
input = sys.stdin.readline
tc = int(input())
for _ in range(tc):
    k = int(input())
    min_h, max_h = [], []
    element_dict = {}
    check_value = set()
    for _ in range(k):
        order = input().split()
        if order[0] == 'D' and order[1] == '-1':
            while min_h:
                if min_h[0] in check_value:
                    x = heapq.heappop(min_h)
                    element_dict[x] -= 1
                    if not element_dict[x]:
                        del element_dict[x]
                        check_value.remove(x)
                    break
                heapq.heappop(min_h)
                
        elif order[0] == "D":
            while max_h:
                if -max_h[0] in check_value:
                    x = -heapq.heappop(max_h)
                    element_dict[x] -= 1
                    if not element_dict[x]:
                        del element_dict[x]
                        check_value.remove(x)
                    break
                heapq.heappop(max_h)
        else:
            x = int(order[1])
            if x not in check_value:
                element_dict[x] = 0
                check_value.add(x)
            heapq.heappush(min_h, x)
            heapq.heappush(max_h, -x)
            element_dict[x] += 1

    if len(check_value) == 0:
        print("EMPTY")
    else:
        min_v = math.inf
        max_v = -math.inf
        for x in check_value:
            min_v = min(min_v, x)
            max_v = max(max_v, x)
        print(max_v, min_v, sep = " ")