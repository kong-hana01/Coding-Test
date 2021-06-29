# https://www.acmicpc.net/problem/15903
# 접근 방법 
# 가장 작은 수끼리 더하면 가장 작은 값이 나오기 때문에 현재 최소 힙 정렬되어있는 힙에서 두 데이터를 뽑은 뒤,
# 주어진 과제를 진행하고(둘을 더하고, 이를 각각의 수에 더해준다.) 힙에 다시 삽입하는 것을 m번만큼 반복한다.

# 시간복잡도
# 최대 카드 합체 횟수 : 15000
# 힙 정렬 사용시 예상되는 최대 시간 : 4(힙 삭제 및 삽입 횟수) x 15000(최대 카드 합체 횟수) x log1000(카드의 개수)
# 대략 60000번의 연산 후 결과 도출 가능


import sys, heapq

n, m = map(int, sys.stdin.readline().split())
card_heap = []

for x in list(map(int, sys.stdin.readline().split())):
    heapq.heappush(card_heap, x)

for _ in range(m):
    card1 = heapq.heappop(card_heap)
    card2 = heapq.heappop(card_heap)
    sum_cards = card1 + card2
    card1 = sum_cards
    card2 = sum_cards
    heapq.heappush(card_heap, card1)
    heapq.heappush(card_heap, card2)

print(sum(card_heap))