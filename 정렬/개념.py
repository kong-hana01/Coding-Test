# 정렬
# 개념 : 데이터를 특정한 기준에 따라 순서대로 나열하는 것
# 종류 : 선택 정렬, 삽입 정렬, 퀵 정렬, 계수 정렬

## 선택 정렬
# 개념 : 처리되지 않은 데이터 중에서 가장 작은 데이터를 선택해 맨 앞에 있는 데이터와 바꾸는 것을 반복한다.
# 시간복잡도 : O(N^2) // 직관적으로 생각해서 하나의 주어진 데이터 정보를 이중 반복문으로 돌리기 때문이다.
# 구현
array = [7, 5, 9, 0, 3, 1, 6, 2, 4, 8]
for i in range(len(array)):
    min_index = array[i] # 가장 앞에 있는 원소의 인덱스
    for j in range(i+1, len(array)):
        if array[min_index] > array[j]: # 현재 min_index보다 더 작은 원소가 있다면 min_index를 바꿔준다.
            min_index = j
    array[min_index], array[i] = array[i], array[min_index]
print(array)


## 삽입 정렬
# 개념 : 처리되지 않은 데이터를 하나씩 골라 적절한 위치에 삽입한다.
# 시간 복잡도 : 최대 O(N^2) // 하지만 리스트가 거의 정렬되어있는 상태라면 O(N)의 시간 복잡도를 가진다.
# 구현 (한번 더 구현해보기)
array = [7, 5, 9, 0, 3, 1, 6, 2, 4, 8]

# 정렬하고자 하는 원소
for i in range(1, len(array)):
    for j in range(i, 0, -1):
        if array[j-1] > array[j]:
            array[j-1], array[j] = array[j], array[j-1]
        else:
            break
print(array)       

## 퀵 정렬
# 개념 : 기준 데이터를 설정하고 그 기준보다 큰 데이터와 작은 데이터의 위치를 바꾸는 방법
# 일반적인 상황에서 가장 많이 사용되는 정렬 알고리즘 중 하나이고 대부분의 프로그래밍 언어의 정렬 라이브러리의 근간이 되는 알고리즘이다.
# 가장 기본적인 퀵 정렬은 첫 번째 데이터를 기준 데이터(Pivot)로 설정한다.
# 시간복잡도 : 평균적으로 O(NlogN) // 하지만 최악의 경우 O(N^2)의 시간복잡도를 가진다. (이미 정렬된 배열에 대해 퀵 정렬을 수행할 경우)
array = [7, 5, 9, 0, 3, 1, 6, 2, 4, 8]

def quick_sort(start, end):
    if start >= end: # 원소가 한 개인 경우에 종료
        return

    pivot = start # 피벗은 첫번째 원소
    left = start + 1
    right = end
    while True:
        # 피벗보다 큰 데이터를 찾을 때까지 반복
        while (left <= end and array[left] < array[pivot]):
            left += 1
        # 피벗보다 작은 데이터를 찾을 때까지 반복
        while (right >= start and array[right] > array[pivot]):
            right -= 1
        # left 인덱스가 right 인덱스보다 작을 때에는 서로 값을 바꿔준다.
        if left < right:
            array[left], array[right] = array[right], array[left]
        # left 인덱스가 right 인덱스보다 큰 경우에는 pivot과 right의 값을 바꿔준다.(pivot기준 왼쪽에는 pivot보다 작은 값들이, 오른쪽에는 pivot보다 큰 값이 있어야하기 때문)
        else:
            array[right], array[pivot] = array[pivot], array[right]
            break
    quick_sort(start, right-1)
    quick_sort(right+1, end)

quick_sort(0, len(array)-1)
print(array)

array = [7, 5, 9, 0, 3, 1, 6, 2, 4, 8]
# 리스트 컴프리핸션 사용
def quick_sort2(array):
    # 리스트가 하나 이하의 원소만을 담고 있다면 종료
    if len(array) <= 1:
        return array
    pivot = array[0] # 피벗은 첫번째 원소

    left_side = [x for x in array[1:] if x <= pivot] # 분할된 왼쪽 부분
    right_side = [x for x in array[1:] if x > pivot] # 분할된 오른쪽 부분

    # 분할 이후 왼쪽 부분과 오른쪽 부분에서 각각 정렬 수행하고, 전체 리스트 반환
    return quick_sort2(left_side) + [pivot] + quick_sort2(right_side) 

print(quick_sort2(array))



## 계수 정렬
# 개념 : 주어진 데이터 크기의 범위가 제한되어있는 경우 그 데이터의 범위만큼 리스트를 생성하고 데이터를 인덱스와 매칭시켜 해당 숫자가 몇번 나왔는지 저장한다.
# 특정한 조건이 부합할 때만 사용할 수 있지만 매우 빠르게 동작하는 정렬 알고리즘이다.
# 데이터의 크기 범위가 제한되어 정수 형태로 표현할 수 있을 때 사용가능하다.
# 시간복잡도와 공간복잡도 : 데이터의 개수가 N, 데이터(양수) 중 최댓값이 K일때 최악의 경우에도 수행시간 O(N + K)를 보장한다.
# 하지만 데이터의 범위가 넓고 데이터의 값들이 분산되어있다면 위와 같은 특성때문에 매우 비효율적이다.
# 동일한 값을 가지는 데이터가 여러개 등장할 때 효율적으로 사용할 수 있다.
#  구현

array = [7, 5, 9, 0, 3, 1, 6, 2, 4, 8, 0]
# 모든 범위를 포함하는 리스트 선언(모든 값은 0으로 초기화)
count = [0 for _ in range(max(array)+1)]

for x in array:
    count[x] += 1 # 각 데이터에 해당하는 인덱스의 값 증가

for i in range(len(count)): # 리스트에 기록된 정렬 정보 확인
    for _ in range(count[i]):
        print(i, end=' ') # 띄어쓰기를 구분으로 등장한 횟수만큼 인덱스 출력
