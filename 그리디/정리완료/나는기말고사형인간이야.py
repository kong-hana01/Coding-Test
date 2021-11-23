# https://www.acmicpc.net/problem/23254
# 접근 방법
# 각 과목마다 기대값을 통해 최대 점수를 계산한다.
# 0. 각 과목 당 공부해서 더 높은 점수를 얻는 과목 순으로 최대 힙 정렬을 한다.
# 1. 최대 힙에서 원소를 하나씩 뺀 뒤, 기댓값과 최댓값을 고려해 나머지가 발생하지 않는 선까지 점수를 더해주고, 기대값을 남은 점수로 바꾼다.
# 2. n이 0이 되거나 최대 힙의 첫 원소의 점수가 만점인 경우에 탐색을 종료하고 최종 성적의 최댓값을 출력한다.
import sys, heapq
input = sys.stdin.readline
n, m = map(int, input().split())
subject_score = list(map(int, input().split()))
subject_plus = list(map(int, input().split()))
subject = []
for i in range(m):
    heapq.heappush(subject, [-subject_plus[i], subject_score[i]])
n *= 24
while subject[0][0] != 0 and n > 0:
    x = heapq.heappop(subject)
    p, s = -x[0], x[1]
    quotient = (100 - s) // p  
    if n >= quotient:
        n -= quotient
    else:
        quotient = n
        n = 0
    s = quotient * p + s
    p = 100 - s
    heapq.heappush(subject, [-p, s])
score = 0
for x in subject:
    score += x[1]
print(score)