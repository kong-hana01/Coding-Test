# 주어진 수를 절반으로 나누어, 수가 작은 쪽은 max_heap으로 구현하고, 수가 큰 쪽은 min_heap으로 구현한다.
import sys, heapq
n = int(sys.stdin.readline())
max_heap = [] # 최대 힙
min_heap = [] # 최소 힙
heapq.heappush(max_heap, -int(sys.stdin.readline())) # 첫 값은 최대 힙에 입력한다.
print(-max_heap[0])
for i in range(n-1): # n-1번만큼 반복
    x = int(sys.stdin.readline()) # 주어진 수를 입력(x)
    
    if len(max_heap) == len(min_heap): # 최대 힙과 최소힙의 길이가 같고
        if -max_heap[0] >= x: # 최대 힙의 가장 큰 데이터(왼쪽 측면에서 가장 큰 데이터)가 x보다 크거나 같을 경우 최대 힙에 x를 삽입하고 그 값을 출력한다.
           heapq.heappush(max_heap, -x)
           print(-max_heap[0])
        else: # 최대 힙의 가장 큰 데이터(왼쪽 측면에서 가장 큰 데이터)가 x보다 작을 경우 최소 힙에 x를 삽입하고 그 값을 출력한다.
            heapq.heappush(min_heap, x)
            print(min_heap[0])

    elif len(max_heap) > len(min_heap): # 최대 힙의 길이가 최소힙의 길이보다 길 때,
        mid = -heapq.heappop(max_heap) # 최대 힙의 데이터를 하나 뽑은 뒤
        if mid > x: # x와 최대 힙에서 뽑은 데이터와 비교해서 x가 더 작을 경우 최대 힙에 x를 삽입하고, 최소 힙에 최대 힙에서 뽑은 데이터를 삽입한다.
            heapq.heappush(max_heap, -x)
            heapq.heappush(min_heap, mid)
        else: # x와 최대 힙에서 뽑은 데이터와 비교해서 x가 더 크거나 같을 경우 다시 최대 힙에 최대 힙에서 뽑은 데이터를 삽입하고, 최소 힙에 x를 삽입한다.
            heapq.heappush(max_heap, -mid)
            heapq.heappush(min_heap, x)
        print(-max_heap[0]) # 삽입 완료 후, 최대 힙에 있는 가장 큰 값을 출력한다. (중간 값)

    else: # 최대 힙의 길이가 최소힙의 길이보다 짧을 때,
        mid = heapq.heappop(min_heap) # 최소 힙의 데이터를 하나 뽑은 뒤
        if mid > x:  # x와 최대 힙에서 뽑은 데이터와 비교해서 x가 더 작을 경우 최대 힙에 x를 삽입하고, 최소 힙에 최대 힙에서 뽑은 데이터를 삽입한다.
            heapq.heappush(max_heap, -x) 
            heapq.heappush(min_heap, mid)
        else: # x와 최대 힙에서 뽑은 데이터와 비교해서 x가 더 크거나 같을 경우 다시 최대 힙에 최대 힙에서 뽑은 데이터를 삽입하고, 최소 힙에 x를 삽입한다.
            heapq.heappush(max_heap, -mid)
            heapq.heappush(min_heap, x)
        print(-max_heap[0]) # 삽입 완료 후, 최대 힙에 있는 가장 큰 값을 출력한다. (중간 값)