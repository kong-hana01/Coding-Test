# 접근방법
# 처음 열에 .인 곳을 모두 1로 바꾼다.
# 이후 열을 하나씩 옮겨가며 해당 열의 데이터를 위에서부터 하나씩 탐색한다. 
# 해당 위치로 올 수 있는 방향(왼쪽 대각선 위, 왼쪽, 왼쪽 대각선 아래)을 차례로 탐색하며 이전 위치에 1이 있다면 해당 위치를 0으로 바꾸고 현재 위치를 1로 바꾼다.
# 이후 마지막 열에서 1의 개수를 모두 세고 이를 출력한다.

import sys
r, c = map(int, sys.stdin.readline().split())
graph = [[x for x in sys.stdin.readline().rstrip()] for _ in range(r)]

for i in range(r):
    if graph[i][0] == '.':
        graph[i][0] = 1
print(graph)

for i in range(1, c):
    for j in range(r):
        if graph[j][i] == '.':
            if j - 1 >= 0 and graph[j-1][i-1] == 1: # 왼쪽 대각선 상단 탐색
                graph[j][i], graph[j-1][i-1] = graph[j-1][i-1], graph[j][i]
            elif graph[j][i-1] == 1: # 왼쪽 탐색
                graph[j][i], graph[j][i-1] = graph[j][i-1], graph[j][i]
            elif j < r - 1 and graph[j+1][i-1] == 1: # 왼쪽 대각선 하단 탐색
                graph[j][i], graph[j+1][i-1] = graph[j+1][i-1], graph[j][i]
            print(f'j 행: {j+1}, i 열: {i+1}, 값: {graph[j][i]}')

count = 0
for i in range(r):
    if graph[i][c-1] == 1:
        count += 1

print(count)