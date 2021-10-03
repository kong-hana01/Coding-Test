# 접근 방법
# 주어진 숫자를 정렬한 뒤 이중 반복문을 통해 숫자를 하나씩 탐색하며 이진탐색을 통해 값을 구한다.
n = int(input())
array = list(map(int, input().split()))
array.sort()
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
            if x == array[j] + array[mid]:
                m = mid
                while i == m or j == m:
                    if m == 0:
                        break
                    m -= 1

                if (i != m and j != m) and (x == array[j] + array[m]):
                    count += 1
                    check = True
                    break
                
                m = mid
                while i == m or j == m:
                    if m == n - 1:
                        break
                    m += 1

                if (i != m and j != m) and (x == array[j] + array[m]):
                    count += 1
                    check = True
                    break

                break
                
            elif x > array[j] + array[mid]:
                start = mid + 1
            else:
                end = mid - 1
        if check:
            break
print(count)