# https://www.acmicpc.net/problem/11497
# 접근 방법 (실버1)
# 0. 통나무의 길이를 오름차순으로 정렬한다.
# 1. 정렬된 통나무를 하나씩 탐색하며 왼쪽으로 추가할 나무와 오른쪽으로 추가할 나무를 하나씩 고려하여 현재 탐색 중인 통나무와 높이 차이가 더 많이 나는 쪽(숫자가 더 작은 쪽)에 해당 통나무를 설치한다. 
# 2. 위의 과정을 반복한 뒤, 모든 탐색을 마치면 최대 높이를 출력한다.

tc = int(input())
for _ in range(tc):
    n = int(input())
    l = list(map(int, input().split()))
    l.sort()
    left, right = l[0], l[0]
    min_difficulty = 0
    for i in range(1, n):
        if left <= right:
            min_difficulty = max(min_difficulty, l[i] - left)
            left = l[i]
        else:
            min_difficulty = max(min_difficulty, l[i] - right)
            right = l[i]

    print(min_difficulty)