# 문제 푼 날짜: 21.08.02
# 차후에 다시 풀어보기
# 접근방법 3
# 0. 집과 사무실의 위치를 오름차순으로 정렬한 뒤, 이 위치 정보들을 이중리스트로 입력받는다.
# 1. 이후 위치 정보의 첫번째 원소를 기준으로 리스트를 정렬한다.
# 2. 리스트의 첫번째 원소의 첫번째 값을 start로, 두번째 값을 end로 초기화한다.
# 3. 리스트의 값을 하나씩 탐색하며 현재 저장되어있는 start+d보다 큰 첫번째 값이 나오기 전까지 다음과 같이 동작하도록 한다.
# 3-1. start+d보다 두번째 값이 작은 경우에는 start_min_heap에 [첫번째 값, 두번째 값]을 저장한다.
# 3-2. start+d보다 두번째 값이 큰 경우에는 end_min_heap에 [두번째 값, 첫번째 값]을 저장한다.
# 4-1. 리스트의 값을 탐색하다 start+d보다 큰 첫번째 값이 나올 경우 start_min_heap의 길이와 현재까지 저장한 count 중 큰 값을 저장하고 start와 첫번째 값이 같은 원소를 pop한다. 그리고 start_min_heap의 첫번째 인덱스의 첫번째 값을 start로 저장한다.
# 4-2. 리스트의 값을 탐색하다 start+d보다 큰 첫번째 값이 나올 경우 start_min_heap의 동작을 한 뒤, end_min_heap에서 첫번째로 저장된 값(end부분)이 start+d보다 작은 경우 이를 pop하고 start_min_heap에 저장한다.
# 5. 위와 같은 과정을 반복하고, 이후 count를 출력한다.

import sys, heapq
from collections import deque
n = int(sys.stdin.readline()) # 사람의 수 입력
array = [sorted(list(map(int, sys.stdin.readline().split()))) for _ in range(n)] # 집과 사무실 위치 입력
d = int(sys.stdin.readline())
array.sort(key=lambda x:x[0])
start = 100000001
count = 0
start_min_heap = []
end_min_heap = []
queue = deque([])

for x1, x2 in array:
    if x2 - x1 <= d:
        start = min(start, x1)
        if not queue or queue[len(queue)-1] != x1:
            queue.append(x1)

        if start+d >= x2:
            # 3-1번
            heapq.heappush(start_min_heap, [x1, x2])
        else:
            # 3-2번
            heapq.heappush(end_min_heap, [x2, x1])
            
            if start+d <= x1:
                # 4-1번
                while start_min_heap:
                    if start_min_heap[0][0] == start:
                        heapq.heappop(start_min_heap)
                    else:
                        break
                
                queue.popleft()
                start = queue[0]
            
                # 4-2번
                while end_min_heap:
                    if end_min_heap[0][0] <= start+d:
                        data = heapq.heappop(end_min_heap)
                        heapq.heappush(start_min_heap, [data[1], data[0]])
                    else:
                        break

        count = max(count, len(start_min_heap))

while end_min_heap:
    if end_min_heap[0][0] <= start+d:
        data = heapq.heappop(end_min_heap)
        heapq.heappush(start_min_heap, [data[1], data[0]])
    else:
        
        while start_min_heap:
            if start_min_heap[0][0] == start:
                heapq.heappop(start_min_heap)
            else:
                break

        queue.popleft()
        start = queue[0]
    count = max(count, len(start_min_heap))
print(count)



# 접근 방법 1
# 1. 집과 사무실의 길이 차이가 최대 d 이내여야지 철로를 놓을 수 있는 대상이 된다. 따라서 리스트 컴프리핸션 정렬을 사용해 대상이 되는 데이터만 따로 정리하고 정렬해 리스트(array)를 만든다.
# 2. 새로 만든 리스트의 개수에 맞게 dp 테이블을 초기화하고, 가장 시작점이 낮은 순서대로 인덱스를 매긴다. 이때 각 인덱스의 원소는 [같은 시작점을 가진 데이터의 개수, 그 시작점부터 d까지 포함되는 데이터 개수]로 설정한다.
# 3. array를 하나씩 탐색하면서 시작 점 값을 저장하고, dp에  각 원소를 하나씩 추가한다.
# 4. array를 탐색하다가 이전 시작 점 값과 같은 경우 같은 시작점을 가진 데이터의 개수를 하나 늘려준다.
# 5. 이후 dp 테이블에서 최대값을 출력한다.

# import sys
# n = int(sys.stdin.readline()) # n 입력
# array = [list(map(int, sorted(sys.stdin.readline().split()))) for _ in range(n)] # 집과 사무실 위치 입력
# d = int(sys.stdin.readline())
# array = [x for x in array if abs(x[0] - x[1]) <= d] # array 내 데이터 중 집과 사무실의 거리가 d 이내인 경우만 저장
# array.sort(key=lambda x:x[0]) # array 내 데이터 최소값으로 정렬

# if array:
#     start = array[0][0]
#     end = array[0][1] 
#     i_1 = 0
#     i_2 = 0
#     i_a = 0

#     dp = [[0, 0] for _ in range(len(array))]
#     dp[0] = [1, 1]

    
#     for x in array[1:]: # array의 데이터를 하나씩 탐색
#         print(dp)
#         if start == x[0]: # 이전의 저장한 start가 같은 경우 dp 테이블의 저장중인 i_1에 1을 더한다.
#             dp[i_1][0] += 1 
#         elif start != x[0]: # 이전에 저장한 start가 x[0]과 다른 경우 dp 테이블의 인덱스를 옮기고 해당 인덱스의 첫번째 원소를 1로 바꾼다.
#             i_1 += 1
#             dp[i_1][0] += 1
#             start = x[0]
        
#         end = x[1] # 가장 거리가 먼 것으로 저장
#         print('end: ', end)
#         print('array[i_a]: ', array[i_a])
#         if end - array[i_a][0] <= d: # 현재 주어진 데이터들을 모두 포괄할 수 있는 길이라면 dp[i_2][1]에 값 누적
#             dp[i_2][1] += 1
            
#         else: # 현재 주어진 데이터들을 모두 포괄할 수 있는 길이가 아니라면 해당 길이가 될 때까지 아래 동작을 반복
#             while end - array[i_a][0] > d:
#                 count = dp[i_2][1] - dp[i_2][0] # dp 테이블에서 i_1의 시작점이 같은 데이터의 개수를 제외한 해당 길이에서부터 d로 포괄가능한 길이의 데이터 개수
#                 i_a += dp[i_2][0] # array 인덱스 증가
#                 i_2 += 1 # dp 테이블 인덱스 증가
#                 dp[i_2][1] = count + 1 # dp 테이블의 누적합 입력

#     print(max(dp, key=lambda x: x[1])[1]) # 최종적으로 누적된 dp 테이블의 값 중 가장 높은 값 출력
# else:
#     print(0)




# 스위핑 알고리즘 배우고 재도전! -> 내가 시도했던 방법이 스위핑 알고리즘의 방식
# 접근방법 2
# 1. 집과 사무실의 길이 차이가 최대 d 이내여야지 철로를 놓을 수 있는 대상이 된다. 따라서 리스트 컴프리핸션 정렬을 사용해 대상이 되는 데이터만 따로 정리하고 정렬해 리스트(array)를 만든다.
# 2. 철로를 하나씩 탐색하며 큐에 삽입한다. 
# 3. 이때 큐에 삽입한 철로의 길이가 d를 초과하면 큐에 삽입한 철로를 뺀다.
# 4. 결과값을 1로 초기화한뒤, 매번 2-3번을 진행할 때마다 결과값과 큐의 길이 중 더 큰 값을 결과값에 저장한다.
# 5. 2-4번의 과정이 끝난 뒤, 결과값을 출력한다.

# import sys
# from collections import deque
# n = int(sys.stdin.readline()) # 사람의 수 입력
# array = [list(map(int, sorted(sys.stdin.readline().split()))) for _ in range(n)] # 집과 사무실 위치 입력
# d = int(sys.stdin.readline()) # 철로의 길이 입력
# array = [x for x in array if abs(x[0] - x[1]) <= d] # array 내 데이터 중 집과 사무실의 거리가 d 이내인 경우만 저장
# array.sort(key=lambda x:x[0]) # array 내 데이터 최소값으로 정렬
# queue = deque([])

# result = 0 # 결과값 0으로 초기화
# for x in array: # 철로를 하나씩 탐색
#     queue.append(x) # 큐에 철로를 삽입

#     while (queue[-1][0] - queue[0][0]) > d: # 큐에 삽입한 철로들의 길이가 d이상일때 큐의 데이터를 하나씩 빼준다.
#         queue.popleft()
#     result = max(result, len(queue))

#     print(queue)
