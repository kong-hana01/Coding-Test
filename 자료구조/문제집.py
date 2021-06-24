'''
위상정렬 배운 뒤, 풀기
import sys, heapq
n, m = map(int, sys.stdin.readline())
first_solve_heap = []
secondary_solve_heap = []
d = [0] * (n+1)
for _ in range(m):
    question1, question2 = map(int, sys.stdin.readline().split())
    heapq.heappush(first_solve_heap, [question1, question2])
    heapq.heappush(secondary_solve_heap, [question2, question1])

for i in range(1, n):
    if d[i] == 0:    
        if i < secondary_solve_heap[0][0] and i < first_solve_heap[0][0]:
            print(i)
        else:
            if i >= first_solve_heap[0][0]:
                question1, question2 = heapq.heappop(first_solve_heap)
'''