# https://www.acmicpc.net/problem/15997
# 접근 방법
# 각각 경기에 대한 확률을 통해 기댓값을 계산해 승점을 계산한다.
# 이후 각 승점에 대한 기댓값을 비교해가며 다음 라운드로 진출할 확률을 출력한다.
# 2위에 해당하는 팀(공동 1위가 3팀 이상인 경우도 해당)이 여럿일 경우 이는 산술평균 내어 확률을 계산한다.

nation = list(input().split())
score = [0 for _ in range(4)]
result = [0 for _ in range(4)]
rank = [1 for _ in range(4)]
for _ in range(6):
    game = list(input().split())
    n1 = nation.index(game[0])
    n2 = nation.index(game[1])
    score[n1] += float(game[2]) * 3 + float(game[3])
    score[n2] += float(game[4]) * 3 + float(game[3])

count = 0
for i in range(4):
    for j in range(4):
        if score[i] < score[j]:
            rank[i] += 1

if rank.count(1) >= 2:
    r = rank.count(1)
    for i in range(4):
        if rank[i] == 1:
            result[i] = 2 / r
else:
    r = rank.count(2)
    for i in range(4):
        if rank[i] == 1:
            result[i] = 1
        if rank[i] == 2:
            result[i] = 1 / r

for x in result:
    print(x)



    