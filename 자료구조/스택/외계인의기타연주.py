# https://www.acmicpc.net/problem/2841
# 접근 방법
# 1. 각 줄별로 stack을 만든 뒤, 주어진 줄과 프렛에 따라 stack에 하나씩 삽입하며 손가락을 움직인 횟수를 한번 더한다.
# 2. 만약 stack에 있는 가장 마지막 원소의 프렛이 지금 연주하고자 하는 음의 프렛보다 높다면 stack에서의 마지막 원소의 프렛이 현재 프렛보다 작아질때까지 pop한다. 그 이후 손가락을 움직인 횟수를 1만큼 더한다.
# 3. 모든 음을 다 탐색한 뒤, 결과를 출력한다.
def move_finger(number, pratt):
    global count
    while dict_stack[number] and dict_stack[number][-1] > pratt:
        dict_stack[number].pop()
        count += 1
    
    if not dict_stack[number] or dict_stack[number][-1] != pratt:
        dict_stack[number].append(pratt)
        count += 1

import sys
input = sys.stdin.readline
n, p = map(int, input().split())
dict_stack = {1: [], 2: [], 3: [], 4: [], 5: [], 6: []}
count = 0

for _ in range(n):
    number, pratt = map(int, input().split())
    move_finger(number, pratt)

print(count)
