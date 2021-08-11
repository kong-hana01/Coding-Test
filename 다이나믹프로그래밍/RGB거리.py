# https://www.acmicpc.net/problem/1149
# 접근 방법
# 1번째 집에서 사용한 페인트의 최솟값은 각각의 페인트 비용과 같다.
# 2번째 집을 칠하면서 누적된 사용한 페인트의 최솟값은 각각 min(1번집에서 사용한 페인트 중 현재 사용할 페인트를 제외한 페인트) + 현재 사용할 페인트의 비용이다.
# 이와 같이 비용을 누적해나가며 칠하다가 마지막 집까지 다 칠하고 난 뒤, 해당 비용 중 가장 작은 것을 출력한다.

n = int(input())
array = [list(map(int, input().split())) for _ in range(n)]
d = [[0, 0, 0] for _ in range(n)]
d[0] = array[0]

for i in range(1, n):
    for j in range(3):
        d[i][j] = min(d[i-1][(j+1) % 3], d[i-1][(j+2) % 3]) + array[i][j]
print(min(d[-1]))