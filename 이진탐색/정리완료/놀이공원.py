# https://www.acmicpc.net/problem/1561
# 접근 방법 (최소 공배수를 구하는 과정이 없이 바로 이진탐색을 진행할 수 있지만 c언어의 최대 정수 크기를 고려해볼 때 문제에서 요구하는 문제 상황과는 다르다고 판단해 이를 나눠준 뒤, 문제를 해결하고자 했다.)
# 주어진 m의 최소 공배수를 구한 뒤, 이를 각 m으로 나눈 값의 합(cycle)을 n에다가 나누어 나머지를 n에다 저장한다.
# 이후 start에 0, end에 cycle을 저장한 뒤, n보다 크거나 같은 인원수가 놀이기구에 탑승할 수 있는 최소 시간(time)을 구한다.
# time - 1을 했을 때의 인원수를 구한 뒤, 놀이기구를 하나씩 탐색하며 인원수가 n이 되는 순간을 구해 해당 놀이기구의 인덱스를 출력한다.
import heapq

def GCD(a, b):
    if a % b == 0:
        return b
    return GCD(b, a%b)

def LCM(a, b):
    return a * b // GCD(a, b)

n, m = map(int, input().split())
array = list(map(int, input().split()))

h = []
for x in array:
    heapq.heappush(h, x)
while len(h) != 1:
    x1 = heapq.heappop(h)
    x2 = heapq.heappop(h)
    heapq.heappush(h, LCM(x2, x1))

gcd = h[0]

cycle = sum([gcd // x for x in array])

n %= cycle
if n == 0:
    print(m)
else:
    start = 0
    end = cycle
    time = cycle
    count = cycle

    while start <= end:
        mid = (start+end) // 2
        total = 0

        for x in array:
            total += (mid // x) + 1

        if total >= n:
            time = min(mid, time)
            count = min(count, total)            
            end = mid - 1

        else:
            start = mid + 1
    count = sum([(time - 1) // x + 1 for x in array])
    for i in range(m):
        if time % array[i] == 0:
            count += 1
            if count == n:
                print(i+1)