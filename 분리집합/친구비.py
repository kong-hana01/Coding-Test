# https://www.acmicpc.net/problem/16562
# 접근 방법
# 분리 집합을 사용해 문제를 해결한다.
# 두 원소들을 합칠 때, 각 원소의 비용을 비교해 더 작은 비용의 원소를 부모 노드로 설정하고, 나머지 비용은 0으로 바꾼 뒤, 분리집합을 진행한다.
# 모든 친구관계를 입력한 뒤, 모든 비용의 합을 계산하고 값이 지금 가지고 있는 돈보다 작으면 이를 출력하고, 크다면 Oh no를 출력한다.
def get_parent(x):
    if student[x] == x:
        return x
    x_ = get_parent(student[x])
    student[x] = x_
    return x_ 

def union_parent(x, y):
    x_ = get_parent(x)
    y_ = get_parent(y)
    if cost[x_] > cost[y_]:
        cost[x_] = 0
        student[x_] = y_
    else:
        cost[y_] = 0
        student[y_] = x_



n, m, k = map(int, input().split())
cost = [0]
for x in list(map(int, input().split())):
    cost.append(x)
student = [i for i in range(n+1)]

for _ in range(m):
    v, w = map(int, input().split())
    union_parent(v, w)

total = sum(cost)
if total <= k:
    print(total)
else:
    print('Oh no')