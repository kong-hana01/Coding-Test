# https://www.acmicpc.net/problem/1713
# 접근 방법
# 완전탐색을 통해 문제를 해결한다.
n = int(input())
recommendCount = int(input())
arr = list(map(int, input().split()))
recommendList = [[0, 0] for _ in range(101)]
for i in range(recommendCount):
    student = arr[i]
    temp = []
    is_in = False
    for j in range(1, 101):
        if recommendList[j][0] > 0:
            temp.append([j, recommendList[j][0], recommendList[j][1]])
            if student == j:
                recommendList[j][0] += 1
                is_in = True
                break
    if is_in:
        continue
    elif len(temp) == n:
        temp.sort(key=lambda x: (x[1], x[2]))
        recommendList[temp[0][0]] = [0, 0]

    recommendList[student] = [1, i]

for i in range(1, 101):
    if recommendList[i][0] > 0:
        print(i, end=' ')
