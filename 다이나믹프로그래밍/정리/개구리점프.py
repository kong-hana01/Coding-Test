# 접근 방법
# 각 통나무에 대한 정보를 입력받을 때 x1, x2, y로 받은 값을 x1, x2, 통나무 번호로 저장한다. y를 저장하지 않는 이유는 x의 값이 겹칠 경우 y와 상관없이 이동할 수 있기때문이다.
# 각 통나무의 번호를 인덱스로 하고 스위핑으로 묶일 수 있는 집합의 번호를 값으로 하는 dp테이블을 초기화한다.
# 통나무에 대한 정보를 x1을 기준으로 오름차순 정렬하고 이를 하나씩 탐색하며 스위핑으로 묶이는 집합을 dp테이블에 입력한다.
# 각 Q에 대해 인덱스를 탐색하며 같은 값이면 1아니면 0을 출력한다.
import sys
input = sys.stdin.readline
n, q = map(int, input().split())
log = []

for i in range(1, n+1):
    x1, x2, y = map(int, input().split())
    log.append([x1, x2, i])
    
dp = [0] * (n+1)

log.sort(key=lambda x: x[0])

number = 1
end = log[0][1]

for x1, x2, i in log:
    if end < x1:
        number += 1
        end = x2
    else:
        end = max(end, x2)
    dp[i] = number

for i in range(q):
    x1, x2 = map(int, input().split())
    if dp[x1] == dp[x2]:
        print(1)
    else:
        print(0)

