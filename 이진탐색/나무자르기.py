# https://www.acmicpc.net/problem/2805
# 접근방법
# 나무의 높이를 오름차순으로 정렬한 뒤, 이진탐색을 통해 특정 길이에 대해 뺀 값의 합을 기준으로 m보다 크면 이를 저장한다.

import sys
n, m = map(int, sys.stdin.readline().split())
trees = list(map(int, sys.stdin.readline().split()))
trees.sort()

start = 0
end = trees[n-1]
result = 0
while start <= end:
    target = (start + end) // 2
    if sum([x-target for x in trees if x-target > 0]) >= m:
        result = max(result, target)
        start = target + 1
    else:
        end = target - 1
print(result)