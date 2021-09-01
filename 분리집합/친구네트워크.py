# https://www.acmicpc.net/problem/4195
# 접근 방법
# 사람의 이름을 key로, 친구로 묶이는 관계를 value로 가지는 딕셔너리를 만들고, 친구로 묶이는 관계의 번호를 인덱스로, 그 관계에 묶이는 인원수를 값으로 가지는 리스트를 만든다.
# 이후 친구가 생길때마다 딕셔너리와 리스트의 값을 조정하고, 친구가 묶일때는 작은 번호의 그룹으로 값을 바꾼다.
# 친구관계를 나타내는 집합은 분리집합을 통해 표현한다.
import sys
input = sys.stdin.readline
sys.setrecursionlimit(10**6)

for _ in range(int(input())):
    f = int(input())
    friend = {}
    name = set()
    numberOfSet = 1
    for _ in range(f):
        f1, f2 = map(int, input().split())
        if f1 not in name:
            friend[f1] = f1
            name.add(f1)
        if f2 not in name:
            friend[f2] = f2
            name.add(f2)
        