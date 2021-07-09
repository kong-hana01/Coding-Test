# https://www.acmicpc.net/problem/7662
# 접근방법
# 1. 최소 힙과 최대 힙을 만든다.
# 2. I는 최소 힙과 최대 힙 둘 다 적용하고 개수를 하나씩 늘려준다.
# 3. D -1은 최소 힙에서 데이터를 삭제한다.
# 4. D  1은 최대 힙에서 데이터를 삭제한다.
# 5. D(삭제명령)을 받았을 때는 개수를 하나씩 삭제하고, 만약 개수가 0이라면 EMPTY를 출력한다.
# 6. 연산이 종료되면 최소 힙과 최대 힙의 원소의 공통된 원소 중 가장 높은 값과 낮은 값을 출력한다.

import heapq, sys
from bisect import bisect_left, bisect_right

def search_check(heap, x):
    left = bisect_left(heap, x)
    right = bisect_right(heap, x)
    print(right, left)
    return right-left


min_heap = []
max_heap = []
for t in range(int(sys.stdin.readline())):
    count = 0
    max_i = 0
    for k in range(int(sys.stdin.readline())):
        order = list(sys.stdin.readline().split())
        if order[0] == 'I':
            heapq.heappush(min_heap, int(order[1]))
            heapq.heappush(max_heap, -int(order[1]))
            count += 1
            # print('삽입:', order[1])
        else:
            if count == 0:
                continue
            elif order[1] == '1':
                while search_check(max_heap, max_heap[0]) > search_check(min_heap, max_heap[0]):
                    heapq.heappop(max_heap)
                x = heapq.heappop(max_heap)
                count -= 1
                # print('max_heap 삭제:', -x)
            else:
                while search_check(max_heap, max_heap[0]) < search_check(min_heap, max_heap[0]):
                    heapq.heappop(min_heap)
                x = heapq.heappop(min_heap)
                count -= 1
                # print('min_heap 삭제:', x)

    if count == 0:
        print('EMPTY')
    else:
        print(-max_heap[0], min_heap[0])

'''
1
8
I 16
I -5643
D -1
D 1
D 1
I 123
D -1
I 124
'''



# import heapq, sys

# for t in range(int(sys.stdin.readline())):
#     array = []
#     count = 0
#     start = 0
#     end = 0
#     for k in range(int(sys.stdin.readline())):
#         order = list(sys.stdin.readline().split())
#         if order[0] == 'I':
#             array.append(int(order[1]))
#             count += 1
#             print('삽입:', order[1])
#         else:
#             if count == 0:
#                 continue
#             elif order[1] == '1':
#                 end += 1
#                 count -= 1
#             else:
#                 start += 1
#                 count -= 1
                
#     if count == 0:
#         print('EMPTY')
#     else:
#         array.sort()
#         print(array[start:len(array)-end])