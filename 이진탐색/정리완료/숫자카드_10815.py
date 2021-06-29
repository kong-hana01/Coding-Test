"""
문제
https://www.acmicpc.net/problem/10815
"""
import sys
from bisect import bisect_right, bisect_left

n = int(sys.stdin.readline())
number_cards = list(map(int, sys.stdin.readline().split())) # 상근이가 가지고 있는 숫자 카드 입력
number_cards.sort() # 이진탐색을 위한 오름차순 정렬
m = int(sys.stdin.readline())
target_numbers = list(map(int, sys.stdin.readline().split())) # 판별해야하는 숫자카드 입력


# 접근 방법 1
# bisect 라이브러리를 활용해 right, left 인덱스 사이에 숫자가 존재하는 지 확인한다.

for target in target_numbers:
    left_index = bisect_left(number_cards, target)
    right_index = bisect_right(number_cards, target)
    if left_index == right_index:
        print(0, end=' ')
    else:
        print(1, end=' ')




# 접근 방법 2
# 이진탐색을 통해 해당 숫자가 존재하는지 확인한다.
# 이진탐색 알고리즘 짜는 걸 연습하기 위해 해당 방법을 사용

# 타겟 숫자를 하나씩 뽑아서 상근이가 가지고 있는 숫자 카드에 있는 지 확인한다.
for target in target_numbers:
    start = 0 # 첫 인덱스
    end = n - 1 # 마지막 인덱스

    while True:
        mid = (end + start) // 2
        # start가 end보다 커질 경우 0을 출력하고 이를 종료한다.
        if start > end:
            print(0, end=' ')
            break
        # 상근이가 가지고 있는 카드의 중간 값이 target보다 클 경우 왼쪽을 탐색한다.
        elif number_cards[mid] > target:
            end = mid-1
        # 상근이가 가지고 있는 카드의 중간 값이 target보다 작을 경우 오른쪽을 탐색한다.
        elif number_cards[mid] < target:
            start = mid+1
        # 상근이가 가지고 있는 카드의 중간 값이 target과 같을 경우 탐색을 종료하고 1을 출력한다.
        elif number_cards[mid] == target:
            print(1, end=' ')
            break

# 접근 방법 3
# set 자료구조를 사용한다.
# set 자료구조는 해쉬값을 사용하기때문에 O(1)이 나온다.
import sys

n = int(sys.stdin.readline())
number_cards = set(map(int, sys.stdin.readline().split())) # 상근이가 가지고 있는 숫자 카드 입력
m = int(sys.stdin.readline())
target_numbers = list(map(int, sys.stdin.readline().split())) # 판별해야하는 숫자카드 입력

for target in target_numbers:
    if target in number_cards:
        print(1, end=' ')
    else:
        print(0, end=' ')