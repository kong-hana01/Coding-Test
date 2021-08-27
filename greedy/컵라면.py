# https://www.acmicpc.net/problem/1781
# 접근 방법
# 0. 주어진 숙제를 데드라인을 기준으로 오름차순 정렬한 뒤, 숙제를 저장할 최소 힙(solve)을 초기화한다.
# 1. 숙제에 대한 정보를 하나씩 탐색하며 solve에 값을 삽입 한다. 
# 1-1. 이때 solve의 길이와 데드라인을 비교해 데드라인과 같다면 solve의 첫번째 원소와 비교해 더 큰 값을 삽입한다.
import heapq, sys
input = sys.stdin.readline
n = int(input())
work = [list(map(int, input().split())) for _ in range(n)]
work.sort()
solve = []

for deadline, count in work:
    if deadline == len(solve):
        if count <= solve[0]:
            continue
        heapq.heappop(solve)
    heapq.heappush(solve, count)
    
print(sum(solve))