# https://www.acmicpc.net/problem/14501
# 접근방법
# 날짜를 인덱스로 하는 dp 테이블 초기화 후, 상담 일정을 하나씩 살펴본 뒤, 해당 날짜에 값을 더한다.
# 모든 상담일정을 다 살펴본 뒤, 상담일자까지의 수익 중 가장 높은 것을 출력한다.

n = int(input())
array = [list(map(int, input().split())) for _ in range(n)]
d = [0] * (n+1) # 최대 N + 5일까지 존재

for i in range(n):
    t, p = array[i]
    for j in range(t+i, n+1):
        d[j] = max(d[j], d[i] + p)
print(d[-1])
