# https://www.acmicpc.net/problem/11497
# 접근 방법 (실버1)
# 0. 정렬한 통나무간의 처음과 끝을 제외한 최대 간격이 얼마인지 확인한다.
# 1. 정렬된 통나무를 하나씩 탐색하며 현재 탐색중인 통나무의 다음 통나무와 가장 높이가 낮은 통나무, 가장 높이가 높은 통나무와 현재 탐색 중인 통나무의 높이 차 중 더 높은 것을 기준으로 최소값을 갱신해나간다.
# 2. 이후 최소값과 0번에서 확인한 간격 중 더 큰 값을 출력한다
tc = int(input())
for _ in range(tc):
    n = int(input())
    l = list(map(int, input().split()))
    l.sort()
    max_length = 0
    for i in range(n-1):
        max_length = max(max_length, abs(l[i] - l[i+1]))
    length = 100000
    for i in range(1, n-1):
        length = min(max(abs(l[i+1]-l[0]), abs(l[i] - l[-1])), length)
        print(f'{i}: {length}')
    print(max(max_length, length))
    print(max_length)