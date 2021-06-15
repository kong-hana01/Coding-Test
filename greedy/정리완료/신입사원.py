# 각 테스트 케이스 마다 서류 심사와 면접 성적을 비교하면 되는 것이기에 단순히 정렬해서 비교하더라도 최대 20 x 100,000 x 2 = 4,000,000번만 돌리면 된다.
import sys

# 테스트 케이스 수 받기
t = int(sys.stdin.readline())
for i in range(t):
    # 인원수 받기
    n = int(sys.stdin.readline())
    # 각 인원에 대한 서류 심사 성적와 면접 시험 성적을 리스트로 하는 이중 리스트
    grade = [list(map(int, sys.stdin.readline().split())) for _ in range(n)]
    # 서류 심사 성적을 기준으로 하는 정렬
    grade.sort(key=lambda x:x[0])
    # 가장 높은 서류 심사 성적을 받은 사람(1등)의 면접 시험 성적을 포인트로 저장
    point = grade[0][1]
    count = 1
    # 모든 인원에 대해 탐색하며 서류 심사에서 자신의 윗 성적을 가진 사람보다 높은 면접 성적을 가진 사람이 있다면 카운트를 하나씩 증가
    for i in range(1, len(grade)):
        if point > grade[i][1]:
            point = grade[i][1]
            count += 1
    print(count)