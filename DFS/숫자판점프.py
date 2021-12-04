# https://www.acmicpc.net/problem/2210
# 접근 방법
# 5x5의 숫자판에서 dfs로 깊이가 6인 판은 모두 탐색한 뒤, 값을 하나씩 찾을 때마다 이를 set에 저장한다.
# 모든 DFS를 마친 뒤, set의 크기를 출력한다.

def dfs(r, c, s, depth):
    s = s + board[r][c]
    if depth == 6:
        if s not in numberSet:
            numberSet.add(s)
        return 
    for dr, dc in [[1, 0], [0, 1], [-1, 0], [0, -1]]:
        if 0<=r+dr<5 and 0<=c+dc<5:
            dfs(r+dr, c+dc, s, depth+1)

board = [list(input().split()) for _ in range(5)]
numberSet = set()
for r in range(5):
    for c in range(5):
        dfs(r, c, '', 1)
print(len(numberSet))