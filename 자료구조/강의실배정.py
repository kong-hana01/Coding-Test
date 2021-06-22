'''
문제
수강신청의 마스터 김종혜 선생님에게 새로운 과제가 주어졌다. 

김종혜 선생님한테는 Si에 시작해서 Ti에 끝나는 N개의 수업이 주어지는데, 최소의 강의실을 사용해서 모든 수업을 가능하게 해야 한다. 

참고로, 수업이 끝난 직후에 다음 수업을 시작할 수 있다. (즉, Ti ≤ Sj 일 경우 i 수업과 j 수업은 같이 들을 수 있다.)

수강신청 대충한 게 찔리면, 선생님을 도와드리자!

입력
첫 번째 줄에 N이 주어진다. (1 ≤ N ≤ 200,000)

이후 N개의 줄에 Si, Ti가 주어진다. (1 ≤ Si < Ti ≤ 109)

출력
강의실의 개수를 출력하라.

'''
# 접근 방법
# 시작시간이 빠른 순서대로 강의를 최소힙 정렬(start_heap)하고 이를 뽑아주며 끝나는 시간이 빠른 순서대로 최소힙 정렬이 된 힙 자료구조(end_heap)에 삽입한다.을 한다. 
# start_heap에서 강의를 뽑았을 때 end_heap에서의 인덱스 0(제일 일찍 끝나는 강의)의 강의를 확인하고 이보다 더 늦게 끝나는 경우 end_heap에 삽입한다.
# start_heap에서 강의를 뽑았을 때 end_heap에서의 인덱스 0(제일 일찍 끝나는 강의)의 강의를 확인하고 이보다 더 빨리 끝나는 경우 인덱스 0인 강의를 삭제하고 start_heap에서 뽑은 강의를 end_heap에 삽입한다.
# 주어진 강의를 모두 확인한 뒤, end_heap의 길이를 확인한 뒤, 이를 출력한다.

import sys, heapq
n = int(sys.stdin.readline())
lecture_list = [list(map(int, sys.stdin.readline().split())) for _ in range(n)]

sys.setrecursionlimit(10**6)

# n = 3
# lecture_list = [[1, 3], [2, 4], [3, 5]]
start_heap = [] # 시작 시간을 우선으로 최소힙 정렬
end_heap = [] # 끝나는 시간을 우선으로 최소힙 정렬(강의실)

for lecture in lecture_list:
    heapq.heappush(start_heap, lecture)

# 강의를 하나 빼서 end_heap(강의실)에 배정한다.
lecture = heapq.heappop(start_heap)
heapq.heappush(end_heap, [lecture[1], lecture[0]])

while start_heap:
    # 강의 시간이 빠른 순서로 정렬된 start_heap에서 강의를 하나 뺀다. (현재 주어진 강의 시간 중 강의의 시작 시간이 가장 빠른 순서대로)
    lecture = heapq.heappop(start_heap)

    # 이미 강의실에 배정된 강의의 끝나는 시간보다 lecture의 시작시간이 더 늦을 경우, end_heap에서 원소를 삭제한 뒤, lecture를 삽입한다.
    if end_heap[0][0] <= lecture[0]:
        heapq.heappop(end_heap)
    heapq.heappush(end_heap, [lecture[1], lecture[0]])

print(len(end_heap))