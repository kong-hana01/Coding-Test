# 05.20
# https://www.acmicpc.net/problem/18116
# 접근 방법
# 분리집합을 통해 로봇의 부품 집합을 계산한다.
def get_parent(node):
    if node == parts[node]:
        return node
    parts[node] = get_parent(parts[node])
    return parts[node]

def find_union(node1, node2):
    parent1 = get_parent(node1)
    parent2 = get_parent(node2)
    if parent1 != parent2:
        parts[parent1] = parent2
        counts[parent2] += counts[parent1]

def count_union(node):
    parent = get_parent(node)
    return counts[parent] 

import sys
sys.setrecursionlimit(10**6)
input = sys.stdin.readline
n = int(input())
parts = [i for i in range(int(1e6)+1)]
counts = [1 for _ in range(int(1e6)+1)]
for _ in range(n):
    query = input().split()
    if query[0] == 'I':
        find_union(int(query[1]), int(query[2]))
    elif query[0] == 'Q':
        print(count_union(int(query[1])))