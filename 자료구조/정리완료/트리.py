# https://www.acmicpc.net/problem/1068
# 접근 방법
# 트리를 해당 노드를 key로 가지고 자식 노드를 value로 가지는 딕셔너리를 통해 구현한다.
# 이후 루트 노드에서부터 자식 노드를 DFS를 통해 하나씩  탐색하며, 리프노드에 도달할 경우 1씩 더해주고, 지울 노드의 번호는 탐색하지 않는다.
# 모든 탐색을 진행한 뒤, 총 몇개의 리프노드가 있었는지 출력한다.
def dfs(root):
    global count 
    if not tree[root]:
        count += 1
    for x in tree[root]:
        if x == remove_node:
            if len(tree[root]) == 1:
                count += 1
            continue
        dfs(x)

n = int(input())
tree = {}
array = list(map(int, input().split()))
remove_node = int(input())
count = 0
for i in range(n):
    if array[i] == -1:
        root = i
    tree[i] = []

for i in range(n):
    if root == i:
        continue
    tree[array[i]].append(i)

if root == remove_node:
    print(0)
else:
    dfs(root)
    print(count)