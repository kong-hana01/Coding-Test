# https://www.acmicpc.net/problem/2170
n = int(input())
array = [list(map(int, input().split())) for _ in range(n)]
array.sort(key = lambda x: x[0])

start, end = array[0][0], array[0][1]
result = 0
if len(array) > 1:
    for a, b in array[1:]:
        if end < b:
            if end < a:
                result += end - start
                start = a
            end = b
    result += end - start
else:
    result = end - start
print(result)