# 각 테스트 케이스 마다 서류 심사와 면접 성적을 비교하면 되는 것이기에 단순히 정렬해서 비교하더라도 최대 20 x 100,000 x 2 = 4,000,000번만 돌리면 된다.
import sys

t = int(sys.stdin.readline())
for i in range(t):
    n = int(sys.stdin.readline())
    grade = [list(map(int, sys.stdin.readline().split())) for _ in range(n)]
    grade.sort(key=lambda x:x[0])
    point = grade[0][1]
    count = 1
    for i in range(1, len(grade)):
        if point > grade[i][1]:
            point = grade[i][1]
            count += 1
    print(count)