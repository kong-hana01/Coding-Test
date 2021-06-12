import sys
sys.setrecursionlimit(3000)

def dfs(x, y, count):
    # count : 0부터
    array[y][x] = count + 2

    for dx, dy in [[1, 0], [-1, 0], [0, 1], [0, -1]]:
        if 0<=x+dx<=m-1 and 0<=y+dy<=n-1 and array[y+dy][x+dx] == 1:
            dfs(x+dx, y+dy, count)

            
t = int(sys.stdin.readline())
for _ in range(t):
    m, n, k = map(int, sys.stdin.readline().split())
    array = [[0 for _ in range(m)] for _ in range(n)]
    for _ in range(k):
        x, y = map(int, sys.stdin.readline().split())
        array[y][x] = 1

    count = 0
    for x in range(m):
        for y in range(n):
            if array[y][x] == 1:
                dfs(x, y, count)
                count += 1

    print(count)