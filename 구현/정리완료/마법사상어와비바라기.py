# https://www.acmicpc.net/problem/21610
# 접근 방법
# 주어진 조건에 따라 구체적으로 코드를 구현한다. (백준 문제 설명 참고)

n, m = map(int, input().split())
grid = [list(map(int, input().split())) for _ in range(n)]
magic = [list(map(int, input().split())) for _ in range(m)]
cloud = [[n-1, 0], [n-1, 1], [n-2, 0], [n-2, 1]]

def move(d, s, cloud):
    # 왼쪽 방향으로 이동
    if d == 1:
        cloud = [[x[0], (x[1]-s) % n] for x in cloud]
    # 왼쪽 위 대각선 방향으로 이동
    elif d == 2:
        cloud = [[(x[0]-s) % n, (x[1]-s) % n] for x in cloud]
    # 윗 방향으로 이동
    elif d == 3:
        cloud = [[(x[0]-s) % n, x[1]] for x in cloud]
    # 오른쪽 위 대각선 방향으로 이동
    elif d == 4:
        cloud = [[(x[0]-s) % n, (x[1]+s) % n] for x in cloud]
    # 오른쪽 방향으로 이동
    elif d == 5:
        cloud = [[x[0], (x[1]+s) % n] for x in cloud]
    # 오른쪽 아래 대각선 방향으로 이동
    elif d == 6:
        cloud = [[(x[0]+s) % n, (x[1]+s) % n] for x in cloud]
    # 아래로 이동
    elif d == 7:
        cloud = [[(x[0]+s) % n, x[1]] for x in cloud]
    # 왼쪽 아래 대각선 방향으로 이동
    elif d == 8:
        cloud = [[(x[0]+s) % n, (x[1]-s) % n] for x in cloud]
    return cloud

def rain_drop():
    for r, c in cloud:
        grid[r][c] += 1

def water_copy():
    for r, c in cloud:
        count = 0
        for dr, dc in [[-1, -1], [-1, 1], [1, -1], [1, 1]]:
            if 0<=r+dr<=n-1 and 0<=c+dc<=n-1 and grid[r+dr][c+dc] > 0:
                count += 1
        grid[r][c] += count

def generator_cloud(cloud):
    new_cloud = []
    grid_cloud = [[0 for _ in range(n)] for _ in range(n)]
    for r, c in cloud:
        grid_cloud[r][c] = 1
    
    for r in range(n):
        for c in range(n):
            if grid[r][c] >= 2 and grid_cloud[r][c] == 0:
                new_cloud.append([r, c])
                grid[r][c] -= 2
    return new_cloud


for d, s in magic:
    cloud = move(d, s, cloud)
    rain_drop()
    water_copy()
    cloud = generator_cloud(cloud)

result = 0
for r in range(n):
    for c in range(n):
        result += grid[r][c]
print(result)