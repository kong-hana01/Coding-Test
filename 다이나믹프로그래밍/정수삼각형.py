n = int(input())
graph = [list(map(int, input().split())) for _ in range(n)]
d = [[0 for _ in range(i)] for i in range(1, n+1)]
for i in range(n):
    d[n-1][i] = graph[n-1][i]


def find_max_value(depth, index):
    if depth == n-1 or d[depth][index]:
        return d[depth][index]

    max_value = 0
    for i in range(index, index+2):
        value = find_max_value(depth+1, i)
        max_value = max(value, max_value)
    d[depth][index] = max_value + graph[depth][index]
    return d[depth][index]

find_max_value(0, 0)
print(d[0][0])