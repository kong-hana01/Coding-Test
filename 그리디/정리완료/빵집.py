# 접근방법
# 이후 열을 하나씩 옮겨가며 해당 열의 데이터를 위에서부터 하나씩 DFS 탐색한다. 
# 해당 위치로 올 수 있는 방향(왼쪽 대각선 위, 왼쪽, 왼쪽 대각선 아래)을 차례로 탐색하며 아직 탐색하지 않은 위치일 경우 DFS 탐색을 하고, 이전에 탐색했던 위치일 경우 탐색하지 않는다.
# 이후 파이프를 놓을 수 있는 개수를 출력한다.

def dfs(row, col):
    graph[row][col] = 'x'
    if col == c-1:
        return True
    for dr, dc in [[-1, 1], [0, 1], [1, 1]]:
        if 0<=row+dr<=r-1 and 0<=col+dc<=c-1 and graph[row+dr][col+dc] == '.' and dfs(row+dr, col+dc):
            return True
    return False



import sys
r, c = map(int, sys.stdin.readline().split())
graph = [[x for x in sys.stdin.readline().rstrip()] for _ in range(r)]

count = 0
for i in range(r):
    if dfs(i, 0):
        count += 1
print(count)

# print(graph)


# for i in range(1, c):
#     for j in range(r):
#         if graph[j][i] == '.':
#             if j - 1 >= 0 and graph[j-1][i-1] == 1: # 왼쪽 대각선 상단 탐색
#                 graph[j][i], graph[j-1][i-1] = graph[j-1][i-1], graph[j][i]
#             elif graph[j][i-1] == 1: # 왼쪽 탐색
#                 graph[j][i], graph[j][i-1] = graph[j][i-1], graph[j][i]
#             elif j < r - 1 and graph[j+1][i-1] == 1: # 왼쪽 대각선 하단 탐색
#                 graph[j][i], graph[j+1][i-1] = graph[j+1][i-1], graph[j][i]
#             print(f'j 행: {j+1}, i 열: {i+1}, 값: {graph[j][i]}')
