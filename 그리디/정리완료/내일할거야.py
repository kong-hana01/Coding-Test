# https://www.acmicpc.net/problem/7983
# 접근방법
# 0. 주어진 과제를 마무리해야하는 시간을 기준으로 내림차순으로 정렬한다.
# 1. 과제를 하나씩 탐색하며 과제를 마무리할 수 있는 시간을 다음과 같이 설정한다.
# min(현재 탐색 중인 과제의 t, 현재까지 저장된 여유시간) - 현재 탐색 중인 과제의 d
# 2. 모든 탐색이 끝난 뒤, 과제를 마무리할 수 있는 최대한 늦은 시간을 출력한다.
import sys
input = sys.stdin.readline
n = int(input())
work = [list(map(int, input().split())) for _ in range(n)]
work.sort(key=lambda x: x[1], reverse = True)
spare_time = work[0][1]
for i in range(n):
    spare_time = min(work[i][1], spare_time) - work[i][0]
print(spare_time)