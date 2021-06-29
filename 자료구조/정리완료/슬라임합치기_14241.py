# 문제 : https://www.acmicpc.net/problem/14241
# 접근 방법
# 슬라임의 크기에 따라 최대 힙 정렬을 한 뒤, 두 개의 데이터를 뽑고 이를 주어진 식에 따라 계산한다.
# 계산 후, 다시 최대 힙에 삽입한다. 
# 이를 반복하다 슬라임이 하나 남았을 때, 그 수를 출력한다.
# 시간복잡도 : O(logN)

import heapq, sys
input = sys.stdin.readline

n = int(input()) # 슬라임 개수 입력받기
slime = list(map(int, input().split())) # 슬라임 크기 입력받기
heap = []
for x in slime:
    heapq.heappush(heap, -x) # 최대 힙 정렬

score = 0 # 점수 초기화
while len(heap) != 1: # 슬라임이 하나남을 때까지 반복
    s1 = heapq.heappop(heap) # 가장 크기가 큰 슬라임 (음수)
    s2 = heapq.heappop(heap) # 두번째로 크기가 큰 슬라임 (음수)
    score += s1*s2 # 점수 계산, 음수 * 음수 = 양수
    heapq.heappush(heap, (s1 + s2)) # 합친 슬라임 다시 삽입하기

print(score) # 점수 출력