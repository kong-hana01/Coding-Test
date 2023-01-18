# https://www.acmicpc.net/problem/12886
# 접근 방법
# 주어진 돌을 작은 쪽의 개수 *  (1001**2) + 중간쪽의 개수  * (1001) + 큰 쪽의 개수로 치환한 뒤, 이를 set에 넣어가며 값을 검토한다.
def trasfer_value(arr):
    num = (arr[0] * (1001**2)) + (arr[1] * (1001)) + arr[2]
    return num

def create_arr(arr, i, j, k):
    if arr[i] < arr[k]:
        x = arr[i]
        y = arr[k]
    else:
        x = arr[k]
        y = arr[i]
    num1 = x + x
    num2 = y - x
    arr = [num1, arr[j], num2]
    arr.sort()
    return arr

def check_same_cnt():
    arr = queue[0]
    return arr[0] == arr[1] == arr[2]

from collections import deque
arr = list(map(int, input().split()))
arr.sort()
queue = deque([])
queue.append(arr)
check = set([])
check.add(trasfer_value(arr))
while queue and not check_same_cnt():
    arr = queue.popleft()
    for x, y, z in [[0, 1, 2], [0, 2, 1], [1, 2, 0]]:
        arr = create_arr(arr, x, y, z)
        num = trasfer_value(arr)
        if num in check:
            continue
        check.add(num)
        queue.append(arr)
    
if queue and check_same_cnt():
    print(1)
else:
    print(0)