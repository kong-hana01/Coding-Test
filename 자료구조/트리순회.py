# https://www.acmicpc.net/problem/1991
# 클래스를 통해 트리 구현(21.08.17) // 딕셔너리를 통한 구현도 해보기
class NodeBT(object):
    
    def __init__(self, value):
        self.value = value
        self.left = None
        self.right = None
    
    def preorder_traversal(self):
        print(self.value, end='')
        if self.left: 
            self.left.preorder_traversal()
        if self.right: 
            self.right.preorder_traversal()

    def inorder_traversal(self):
        if self.left:
            self.left.inorder_traversal()
        print(self.value, end='')
        if self.right:
            self.right.inorder_traversal()
    
    def postorder_traversal(self):
        if self.left:
            self.left.postorder_traversal()
        if self.right:
            self.right.postorder_traversal()
        print(self.value, end='')


node = [chr(i) for i in range(ord('A'), ord('A')+26)]

n = int(input())
array = [list(input().split()) for _ in range(n)]
for i in range(n):
    value = array[i][0]
    index = ord(value) - ord('A')
    node[index] = NodeBT(value)
    
for i in range(n):
    value, left, right = array[i]
    subtree_root = node[ord(value) - ord('A')]
    if left != '.':
        left_index = ord(left) - ord('A')
        subtree_root.left = node[left_index]
    if right != '.':
        right_index = ord(right) - ord('A')
        subtree_root.right = node[right_index]

node[0].preorder_traversal()
print()
node[0].inorder_traversal()
print()
node[0].postorder_traversal()
