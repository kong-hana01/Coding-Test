import sys
n, m = map(int, sys.stdin.readline().split())
array = [list(map(int, sys.stdin.readline().split())) for _ in range(n)]

for x in range(n):
    for y in range(m):
        step = [[x, y]]
        temp = array[x][y]
        for dx1, dy1 in [[1, 0], [0, 1], [-1, 0], [0, -1]]:
            x2 = x+dx1
            y2 = y+dy1
            if 0<=x2<=n-1 and 0<=y2<=m-1:
                step.append([x2, y2])
                temp += array[x2][y2]
                for dx2, dy2 in [[1, 0], [0, 1], [-1, 0], [0, -1]]:
                    x3 = x2+dx2
                    y3 = y2+dy2        
                    if 0<=x3<=n-1 and 0<=y3<=m-1 and [x3, y3] not in step:
                        step.append([x3, y3])
                        temp += array[x3][y3]   
                        for dx3, dy3 in [[1, 0], [0, 1], [-1, 0], [0, -1]]:
                            x4 = x3+dx3
                            y4 = y3+dy3                   
                            if 0<=x4<=n-1 and 0<=y4<=m-1 and [x4, y4] not in step:
                                step.append([x4, y4])
                                if temp + array[x4][y4] > result:
                                    result = temp + array[x4][y4]
                        temp -= array[x3][y3] 
                temp -= array[x2][y2]

print(result)
