# https://www.acmicpc.net/problem/4195
# 접근 방법
# 0. 이름을 key로 하고, 그 이름에 해당하는 인덱스를 value로 가지는 딕셔너리를 만든다. 그리고 최대 F * 2개의 리스트를 두 개 만들어 하나는 친구 관계의 인원수를 세고, 나머지는 친구 관계의 집합을 표현한다. 
# 1. 유니온 파인드를 통해 그룹을 나누어 만들고, 부모 노드에 대해 친구 관계의 수를 갱신해주며 그 값을 결과값에 최대값을 갱신하며 저장한다.
def get_parent(idx):
    if parent[idx] == idx:
        return idx
    index = get_parent(parent[idx])
    parent[idx] = index
    return index

def find_union(p1, p2):
    x1 = get_parent(p1)
    x2 = get_parent(p2)
    if x1 < x2:
        parent[x2] = x1
        total[x1] += total[x2]
        total[x2] = 0
        return total[x1]    
    elif x1 > x2:
        parent[x1] = x2
        total[x2] += total[x1]
        total[x1] = 0
        return total[x2]
    return total[x1]

import sys
input = sys.stdin.readline
for tc in range(int(input())):
    f = int(input())
    parent = [i for i in range(f*2)]
    total = [1 for i in range(f*2)]
    name_set = set()
    name_dict = {}
    idx = 0
    for _ in range(f):
        p1, p2 = input().split()
        if p1 not in name_set:
            name_dict[p1] = idx
            idx += 1
            name_set.add(p1)
        if p2 not in name_set:
            name_dict[p2] = idx
            idx += 1
            name_set.add(p2)
        count = find_union(name_dict[p1], name_dict[p2])
        print(count)