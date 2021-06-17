## 탐색
# 특정한 데이터를 찾기위해 데이터를 찾는 과정
# 순차 탐색 : 리스트 안에 있는 특정한 데이터를 찾기 위해 앞에서부터 데이터를 하나씩 확인하는 방법
# 시간복잡도 : O(N^2)

# 이진 탐색 : 정렬되어있는 리스트에서 탐색 범위를 절반씩 좁혀가며 데이터를 탐색하는 방법
#   * 이진 탐색은 시작점, 끝점, 중간점을 이용하여 탐색 범위를 설정한다.
# 시간복잡도 : O(LogN)
# 구현 1 : 재귀적 구현

n, target = 10, 7 # 원소의 개수, 찾고자 하는 값
array = [1, 3, 5, 7, 9, 11, 13, 15, 17, 19]
def binary_search(start, end, target):
    if start > end:
        return False
    mid = (end+start)//2
    
    # 중간점의 값보다 찾고자하는 값이 작은 경우 왼쪽 확인
    if array[mid] > target:
        return binary_search(start, mid-1, target)
        
    # 중간점의 값보다 찾고자하는 값이 큰 경우 오른쪽 확인
    elif array[mid] < target:
        return binary_search(mid+1, end, target)

    # 찾은 경우 중간점 인덱스 반환
    elif array[mid] == target:
        return mid

result = binary_search(0, n-1, target)
if result:
    print(result + 1)
else:
    print('원소가 존재하지 않습니다.')


def binary_search2(target, start, end):
    while True:
        if start > end:
            return False
        mid = (start+end) // 2

        # 중간점의 값보다 찾고자하는 값이 작은 경우 왼쪽 확인
        if array[mid] > target:
            end= mid-1 

        # 중간점의 값보다 찾고자하는 값이 큰 경우 오른쪽 확인
        elif array[mid] < target:
            start = mid+1

        # 찾은 경우 중간점 인덱스 반환    
        else:
            return mid

result = binary_search2(target, 0, n-1)
if result:
    print(result + 1)
else:
    print('원소가 존재하지 않습니다.')


# 값이 특정 범위에 속하는 데이터 개수 구하기
# bisect_left(array, x) : 정렬된 순서를 유지하면서 배열 array에 x를 삽입할 가장 왼쪽 인덱스를 반환
# bisect_right(array, x) : 정렬된 순서를 유지하면서 배열 array에 x를 삽입할 가장 오른쪽 인덱스를 반환
from bisect import bisect_left, bisect_right

def count_by_range(array, left_value, right_value):
    right_index = bisect_right(array, right_value)
    left_index = bisect_left(array, left_value)
    return right_index - left_index

# 배열 선언
a = [1, 2, 3, 3, 3, 3, 4, 4, 8, 9]

# 값이 4인 데이터 개수 출력
print(count_by_range(a, 4, 4))

# 값이 [-1, 3] 범위에 있는 데이터 개수 출력
print(count_by_range(a, -1, 3))