# 접근 방법
# 키를 기준으로 하는 최대 힙에 학생을 모두 삽입한다.
# 모든 학생들에 대해 오름차순으로 정렬한 뒤, 최소 등수가 1이될 때까지 최대 힙에 있는 학생을 삭제하고, 1이 되었을 때 팀의 개수를 늘려준다.
# 현재 탐색 중인 학생과 최대 힙에서 삭제한 값이 같을 경우(키를 기준으로) 탐색을 종료하고 팀의 개수를 출력한다.

import sys, heapq
n = int(sys.stdin.readline())
array = [list(map(int, sys.stdin.readline().split())) for _ in range(n)]
array.sort()

h = []
for x in array:
    heapq.heappush(h, -x[0]) # 키를 기준으로 하는 최대 힙 
 
team = 1 # 팀 개수 초기화
for height, min_rank in array:
    while min_rank > 1 and height <= -h[0]:
        x = heapq.heappop(h)
        min_rank -= 1
    
    if not h or height >= -h[0]:
        break
    team += 1
print(team)