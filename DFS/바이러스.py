import sys


# n = int(sys.stdin.readline())
# pair = int(sys.stdin.readline())
# graph = [list(map(int, sys.stdin.readline().split())) for _ in range(pair)]

n = 5
pair = 4
#graph = [[1, 2], [2, 3], [1, 5], [5, 2], [5, 6], [4, 7]]
#graph = [[2, 1], [2, 3], [5, 1], [5, 2], [5, 6], [4, 7]]
graph = [[4, 5], [3, 4], [1, 2], [2, 3]]
#graph = [[4, 3], [1, 3], [2, 4], [2, 3]]
#graph = [[3, 4], [4, 5], [5, 6], [1, 2], [2, 3]]
#graph = [[1, 3], [2, 3]]
#graph = [[6, 5], [5, 4], [4, 3], [3, 2], [2, 1]]


visited = [False] * pair
target = [1]


# def dfs(count=0):
#     i = 0
#     while True:
#         if target[-1] in graph[i] and not visited[i]:
#             break
#         elif i >= n-1:
#             target.pop()
#             return dfs(count)
#         i += 1
#     v = i       

#     visited[v] = True

#     for x in graph[v]:
#         if x not in target:
#             count += 1
#             print(x)
#             target.append(x)
#             return dfs(count)
    
#     return count

# print(dfs())

# 구현
# def implementation(index):
#     """
#     index : graph와 visited의 인덱스
#     """    
    
#     if not visited[index]:
#         visited[index] = True
#         if graph[index][0] in target or graph[index][1] in target:
#             for x in graph[index]:
#                 if x not in target:
#                     target.append(x)

# for i in range(pair):
#     implementation(i)

# print(len(target) - 1)


'''
# dfs
def dfs(v, index=0):
    # v : 타겟값 / index : graph와 visited의 인덱스
    
    if not visited[index]:
        if v in graph[index]:
            for x in graph[index]:
                if x not in target:
                    target.append(x)
                    print(x)
                    visited[index] = True
                    for i in range(len(graph)):
                       if not visited[i]:
                           dfs(x, i)
i = 0                      
while True:
    if len(target) >= 2 or i > len(graph):
        break
    dfs(1, i)
    i += 1

#print(dfs(1))
print(len(target)-1)
'''

def dfs(v, index=0):
    # v : 타겟값 / index : graph와 visited의 인덱스
    for index in range(len(graph)):
        if not visited[index]:
            if v in graph[index]:
                for x in graph[index]:
                    if x not in target:
                        target.append(x)
                        print(x)
                        visited[index] = True
                        dfs(x, index)
                            

dfs(1)
print(len(target)-1)