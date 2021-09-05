# https://www.acmicpc.net/problem/4358
# 접근 방법
# 딕셔너리를 통해 종의 이름을 키로 갖고, 그 개수를 값으로 갖는 tree를 만든다.
# 이후 전체 개수에 대해 반올림을 한 뒤, 종별로 그 비율을 출력한다.
import sys
input = sys.stdin.readline
tree = {}
s = set()
count = 0
while True:
    t = input().rstrip()
    if not t:
        break
    if t not in s:
        tree[t] = 0
    tree[t] += 1
    count += 1
    s.add(t)

name = []
for x in tree.keys():
    name.append(x)
name.sort()

# for x in name:
#     print(x, round(tree[x] / count * 100, 4))
for x in name:
    print(x, '%.4f' % (tree[x] / count * 100))