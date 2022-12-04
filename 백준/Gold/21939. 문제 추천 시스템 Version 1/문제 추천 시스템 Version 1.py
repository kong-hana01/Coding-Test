# https://www.acmicpc.net/problem/21939
# 접근 방법
# 난이도를 인덱스로 하는 이중 리스트와
# 문제번호를 키로 하고, 난이도를 값으로 가지는 딕셔너리를 활용해 문제를 해결한다.
def recommend(x):
    if x == -1:
        idx = 0
        diff = 1
        step = 1
    else:
        idx = 1
        diff = 100
        step = -1
    
    # 빠져나온 시점에 데이터가 있음
    while rank[diff][2] == 0:
        diff += step
    
    while True:
        x = heapq.heappop(rank[diff][idx])
        if problem[abs(x)] == diff:
            heapq.heappush(rank[diff][idx], x)
            return abs(x)

def add(number, difficulty):
    problem[number] = difficulty
    heapq.heappush(rank[difficulty][0], number) # min 힙
    heapq.heappush(rank[difficulty][1], -number) # max 힙
    rank[difficulty][2] += 1

def solved(number):
    diff = problem[number]
    problem[number] = 0
    rank[diff][2] -= 1

import sys, heapq
input = sys.stdin.readline
rank = [[[], [], 0] for _ in range(101)]
problem = {}
n = int(input())
for _ in range(n):
    number, difficulty = map(int, input().split())
    problem[number] = difficulty
    heapq.heappush(rank[difficulty][0], number) # min 힙
    heapq.heappush(rank[difficulty][1], -number) # max 힙
    rank[difficulty][2] += 1

m = int(input())
for _ in range(m):
    command = input().split()
    if command[0] == "add":
        number, difficulty = map(int, command[1:])
        add(number, difficulty)
    elif command[0] == "recommend":
        x = int(command[1])
        print(recommend(x))
    else:
        number = int(command[1])
        solved(number)
