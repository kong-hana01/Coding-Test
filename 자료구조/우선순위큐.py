### 우선순위 큐
# 정리 : https://www.daleseo.com/python-heapq/
# 우선순위 큐는 데이터를 우선순위에 따라 처리하고 싶을 때 사용한다.
# 예시) 물건 데이터를 자료구조에 넣었다가 가치가 높은 물건부터 꺼내서 확인해야하는 경우

# 구현 방법
# 1) 단순히 리스트를 이용하여 구현한다.
# 2) 힙(heap)을 이용하여 구현한다.

# 데이터의 개수가 N개 일 때, 구현 방식에 따라서 시간 복잡도를 비교한 내용은 다음과 같다.
## 리스트 
# - 삽입 시간 : O(1) (리스트의 가장 뒤에 추가가 되기에 O(1)이 소요됨)
# - 삭제 시간 : O(N) (모든 데이터를 확인하기 때문에 선형 시간 복잡도를 가짐)
## 힙
# - 삽입 시간 : O(logN) 
# - 삭제 시간 : O(logN) 
# 단순히 N개의 데이터를 힙에 넣었다가 모두 꺼내는 작업은 정렬과 동일하다. (힙정렬) 따라서 시간 복잡도는 O(NlogN)이다.


## 힙의 특징
# 힙은 완전 이진 트리 자료구조의 일종이다.
# 힙에서는 항상 루트 노드를 제거한다.

# 최소 힙(min heap)
# - 루트 노드가 가장 작은 값을 가진다.
# - 따라서 값이 작은 데이터가 우선적으로 제거된다.

# 최대 힙(max heap)
# - 루트 노드가 가장 큰 값을 가진다.
# - 따라서 값이 큰 데이터가 우선적으로 제거된다.


## 최소 힙 구성 함수 : min-heapify() (힙을 구성하기 위한 함수의 이름을 일반적으로 heapify라고 함)
# 상향식 : 부모 노드로 거슬러 올라가며, 부모보다 자신의 값이 더 작은 경우에 위치를 교체한다.
# 새로운 원소가 삽입되었을 때 O(logN)의 시간 복잡도로 힙 성질을 유지하도록 할 수 있다.
# 원소가 제거되었을 때 O(logN)의 시간 복잡도로 힙 성질을 유지하도록 할 수 있다.
# - 원소를 제거할 때는 가장 마지막 노드가 루트 노드의 위치에 오도록 한다.
# - 이후에 루트 노드에서부터 하향식으로 (더 작은 자식 노드로) Heapify()를 진행한다.

# 힙 정렬 구현 예제
import sys
import heapq # min heap
input = sys.stdin.readline

def heapsort(iterable):
    h = []
    result = []
    # 모든 원소를 차례대로 힙에 삽입
    for value in iterable:
        # h : 힙 
        heapq.heappush(h, value)
    
    # 힙에 삽입된 모든 원소를 차례대로 꺼내어 담기
    for _ in range(len(h)):
        result.append(heapq.heappop(h))
    return result


n = int(input())
arr = []

for i in range(n):
    arr.append(int(input()))

res = heapsort(arr)
for i in range(n):
    print(res[i])