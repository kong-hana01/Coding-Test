# 접근 방법
# 주어진 숫자를 정렬한 뒤 이중 반복문을 통해 숫자를 하나씩 탐색하며 이진탐색을 통해 값을 구한다.
n = int(input())
array = list(map(int, input().split()))
count = 0
for i in range(n):
    x = array[i]
    for j in range(n):
        if i == j:
            continue
        start = 0
        end = n - 1
        check = False
        while start <= end:
            mid = (start+end)//2
            if mid == j or mid == i:
                if array[]
                continue
            if x == array[j] + array[mid]:
                if j != mid or (mid + 1 <= n - 1 and array[mid] ==  array[mid+1]) or (mid - 1 >= 0 and array[mid] == array[mid-1]):
                    count += 1
                    check = True
                    break
                else:
                    break
            elif x > array[j] + array[mid]:
                start = mid + 1
            else:
                end = mid - 1
        if check:
            break
print(count)