# https://www.acmicpc.net/problem/6209
# 접근 방법
# 학생들이 점프하는 최소 거리의 최댓값을 mid로 하는 이진 탐색을 통해 m개의 돌을 없앴을 때, 최소거리의 최댓값을 구한다.
# 각 이진탐색을 할 때마다 없앤 돌의 개수를 센 뒤, 없앤 돌의 개수가 m보다 작다면 start를 mid + 1로, 크다면 end를 mid - 1로한다.
# 없앤 돌의 개수와 m이 같다면 해당 값을 저장한 뒤, start를 mid + 1로 해준다.
import sys
input = sys.stdin.readline
d, n, m = map(int, input().split())
stone = [int(input()) for _ in range(n)]
stone.sort()
start = 0
end = d
dist = 0
while start <= end:
    mid = (start + end) // 2
    count = 0 # 돌의 개수
    now = 0
    min_distance = d
    for x in stone:
        if x - now >= mid:
            min_distance = min(min_distance, x - now)
            now = x
        else:
            count += 1

    min_distance = min(min_distance, d - now)

    if count > m:
        end = mid - 1
    else:
        dist = max(dist, min_distance)
        start = mid + 1

print(dist)