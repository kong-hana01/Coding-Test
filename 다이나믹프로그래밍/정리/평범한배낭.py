# 접근 방법
# 준서가 버틸 수 있는 무게만큼 dp 테이블을 초기화한 뒤, 각 무게마다 가장 가치가 높은 값을 저장한다.
# 1. 물건을 하나씩 탐색하며 dp 테이블의 무게 인덱스 위치에 가치를 저장한다.
# 2. 가치를 저장할 때는 현재 저장되어있는 가치와 저장할 가치 중 더 큰 값을 저장한다.
# 3. 물건을 하나씩 탐색할 때마다 dp 테이블을 탐색하며 값이 들어있는 dp 테이블의 인덱스에 현재 탐색중인 물건의 무게만큼 더한 뒤, 가치를 합산해 저장한다.

import sys
n, k = map(int, sys.stdin.readline().split())
array = [list(map(int, sys.stdin.readline().split())) for _ in range(n)]
dp = [0] * (k+1)
dp_i = set()

dp = [0] * (k+1)
for x in array:
    if x[0] < len(dp):
        temp = [[x[0], x[1]]]
    else:
        temp = []
    for i in dp_i:
        if i+x[0] < len(dp):
            temp.append([i+x[0], dp[i] + x[1]])
    for t in temp:
        dp_i.add(t[0])
        dp[t[0]] = max(dp[t[0]], t[1])
print(max(dp))