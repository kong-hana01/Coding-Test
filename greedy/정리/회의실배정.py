# 정렬 배우고 다시 하기
n = int(input())
array = [list(map(int, input().split())) for _ in range(n)]
#n = 11
#array = [[1, 4],[3, 5],[5, 6],[6, 7],[3, 8],[5, 9],[6, 10],[8, 11],[8, 12],[2, 13],[12, 14]]
#array = [[8, 8],[5, 8],[3, 4], [2, 5], [2, 7], [8, 8], [1, 10], [3, 3], [10, 10]]
#print(sorted(array, key=lambda x: (x[0], x[1])))

# 방법 1
for i, value in enumerate(sorted(array, key=lambda x: (x[0], x[1]))):
    if i == 0:
        result = 1
        meeting = value
        point = i
    elif meeting[1] > value[1]:
        meeting = value
        point = i
    elif meeting[1] <= value[0] and point != i:
        meeting = value
        point = i
        result += 1

    
print(result)


# 방법 2
dic = {}
for k, v in array:
    if k not in dic.keys():
        dic[k] = [v]
    else:
        dic[k].append(v)

result = 1
meeting = [0] * 2
for i, start in enumerate(sorted(dic)):
    for j, end in enumerate(sorted(dic[start])):
        if meeting[1] > end or i == j == 0:
            meeting = [start, end]
            point = [i, j]
        elif meeting[1] <= start and point != [i, j]:
            meeting = [start, end]
            point = [i, j]
            result += 1


print(result)