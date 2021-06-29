# 접근방법
# 주어진 점들을 두개씩 탐색하면서 정확히 절반이 되는 값이 주어진 점들 가운데에 있는 지 확인한다.
# 해당 문제의 시간 복잡도 : O(N^2 * logN) = 최대 약 1000만번 연산
# 다음번에 O(N * logN)으로 풀 수 있는 방법을 고안하기

from bisect import bisect_right, bisect_left
import sys

def check_dot(dots, dot):
    right_index = bisect_right(dots, dot)
    left_index = bisect_left(dots, dot)
    if right_index == left_index:
        return 0
    return 1


t = int(sys.stdin.readline())
for _ in range(t):
    n = int(sys.stdin.readline())
    dots = list(map(int, sys.stdin.readline().split()))
    dots.sort()
    count = 0
    for i in range(len(dots)):
        for j in range(i+2, len(dots)):
            if (dots[i] + dots[j]) % 2 == 0:
                dot = (dots[i] + dots[j]) // 2
                count += check_dot(dots, dot)
    print(count)
