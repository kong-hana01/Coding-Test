import sys
#n = int(sys.stdin.readline())
#graph = [list(map(int, sys.stdin.readline()[:n])) for _ in range(n)]
n = 7
graph = [[0, 1, 1, 0, 1, 0, 0], [0, 1, 1, 0, 1, 0, 1], [1, 1, 1, 0, 1, 0, 1], [0, 0, 0, 0, 1, 1, 1], [0, 1, 0, 0, 0, 0, 0], [0, 1, 1, 1, 1, 1, 0], [0, 1, 1, 1, 0, 0, 0]]
step_ = [[0,1],[0,-1],[1,0],[-1,0]]
num_a = []
#print(graph)

def dfs(x, y, i):
    # i는 2부터 시작
    num_a[i-2] += 1   
    graph[x][y] = i
    for dx, dy in step_:
        new_x = x+dx
        new_y = y+dy
        if 0 <= new_x <= n-1 and 0 <= new_y <= n-1 and graph[new_x][new_y] == 1:
            dfs(new_x,new_y,i)
    
i = 2
for x in range(n):
    for y in range(n):
        if graph[x][y] == 1:
            num_a.append(0)
            dfs(x,y,i)
            i += 1

print(len(num_a))
for num_ in sorted(num_a):
    print(num_)
#print(graph)