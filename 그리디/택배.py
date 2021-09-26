# 접근 방법
# 최소힙과 최대힙을 활용해 트럭이 싣고 가는 택배의 양을 조절한다.
# 현재 탐색 중인 마을보다 낮은 번호의 마을은 최소힙에서 마을 번호를 꺼내 해당 숫자를 더한다.
# 현재 탐색 중인 마을에서 택배를 실을 때 택배의 용량이 초과되면 최대힙에서의 마을 번호에 있는 택배를 뺀다.
import heapq
n, c = map(int, input().split())
m = int(input())
array = [list(map(int, input().split())) for _ in range(m)]
array.sort(key=lambda x: (x[0], x[1]))
now_weight = 0
result = 0
weights = [0 for _ in range(n+1)]
min_h = []
max_h = []
for s, e, w in array:
    while min_h and min_h[0] <= s:
        idx = heapq.heappop(min_h)
        result += weights[idx]
        now_weight -= weights[idx]
        weights[idx] = 0
    while now_weight + w > c and max_h and -max_h[0] > e:
        idx = -heapq.heappop(max_h)
        drop_box = min((now_weight + w) - c, weights[idx])
        if drop_box != weights[idx]:
            heapq.heappush(max_h, -idx)
        weights[idx] -= drop_box
        now_weight -= drop_box
    
    if c >= now_weight + w:
        delivery_box = w
    else:
        delivery_box = w - ((now_weight + w) - c)
    
    weights[e] += delivery_box
    now_weight += delivery_box
    heapq.heappush(min_h, e)
    heapq.heappush(max_h, -e)
print(result + sum(weights))
