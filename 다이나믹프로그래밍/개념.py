### 다이나믹 프로그래밍
## 개념
# 메모리를 적절히 사용하여 수행 시간 효율성을 비약적으로 향상시키는 방법
# 이미 계산된 결과(작은 문제)는 별도의 메모리 영역에 저장하여 다시 계산하지 않도록 한다.
# 다이나믹 프로그래밍의 구현은 일반적으로 두 가지 방식(탑 다운과 바텀 업)으로 구성된다.
# 동적 계획법이라고도 부른다.

# cf) 일반적인 프로그래밍 분야에서 동적이라고 이야기하는 것과는 약간 차이가 있다.
# ex) 자료구조에서 동적 할당은 '프로그램이 실행되는 도중에 실행에 필요한 메모리를 할당하는 기법'을 의미한다.
# 반면 다이나믹 프로그래밍에서 다이나믹은 별다른 의미 없이 사용된 단어이다.


## 사용 조건
# 1. 최적 부분 구조 (Optimal Substructure)
#   - 큰 문제를 작은 문제로 나눌 수 있으며 작은 문제의 답을 모아서 큰 문제를 해결할 수 있다.
# 2. 중복되는 부분 문제 (Overlapping Subproblem)
#   - 동일한 작은 문제를 반복적으로 해결해야한다.

## 피보나치 수열 문제
# 점화식이란 인접한 항들 사이의 관계식을 의미하는데 이를 이용하면 문제를 해결할 수 있다.
# 점화식은 프로그래밍에서 재귀함수를 사용하면 구할 수 있다.
# 또한 수열은 배열이나 리스트를 이용해 표현할 수 있다.

def fibo(x):
    if x == 1 or x == 2:
        return 1
    return fibo(x - 1) + fibo(x - 2)

print(fibo(4))

# 위의 점화식에서의 시간복잡도 : 지수 시간 복잡도 O(2^n)
# 같은 값이 여러번 호출되는 것을 확인할 수 있다. (중복되는 부분 문제)

# 피보나치 수열의 효율적인 해법 : 다이나믹 프로그래밍
# 1. 최적 부분 구조 : 큰 문제를 작은 문제로 나눌 수 있다.
# 2. 중복되는 부분 문제 : 동일한 작은 문제를 반복적으로 해결한다.
# 피보나치 수열은 위의 두 가지 사용 조건을 만족하기 때문에 문제 해결에 다이나믹 프로그래밍을 사용할 수 있다.


## 탑다운(하향식) vs 바탐업(상향식)
# 다이나믹 프로그래밍의 전형적인 형태는 바텀업 방식이다.
#   - 결과 저장용 리스트(배열)는 DP 테이블이라고 부른다.
# 엄밀히 말하면 메모이제이션은 이전에 계산된 결과를 일시적으로 기록해 놓는 넓은 개념을 의미한다.
#   - 따라서 메모이제이션은 다이나믹 프로그래밍에 국한된 개념은 아니다.
#   - 한 번 계산된 결과를 담아 놓기만 하고 다이나믹 프로그래밍을 위해 활용하지 않을 수도 있다.

## 탑다운(하향식) - 메모이제이션(Memoization)
# 한 번 계산한 결과를 메모리 공간에 메모하는 기법이다.
#   - 같은 문제를 다시 호출하면 메모했던 결과를 그래도 가져온다.
#   - 값을 기록해 놓는 다는 점에서 캐싱(Caching)이라고도 한다. 이때 대부분의 다이나믹프로그래밍을 위해 사용하는 배열은 Memo, table, DP, D라고 표현한다.
# 재귀적인 방법으로 사용한다.

## 바텀업(상향식)
# 반복문을 이용해서 사용한다.



## 탑다운 다이나믹 프로그래밍으로 해결한 피보나치 수열
# 한 번 계산된 결과를 메모이제이션하기 위한 리스트 초기화
d = [0] * 100

# 피보나치 함수를 재귀함수로 구현 (탑다운 다이나믹 프로그래밍)
def fibo(x):
    # 종료조건 (1 혹은 2일 때 1을 반환)
    if x == 1 or x == 2:
        return 1
    # 이미 계산한 적 있는 문제라면 그대로 반환
    if d[x] != 0:
        return d[x]

    # 아직 계산하지 않은 문제라면 점화식에 따라서 피보나치 결과 반환
    d[x] = fibo(x - 1) + fibo(x - 2)
    return d[x]

print(fibo(99))

# 메모이제이션의 시간 복잡도 : O(N)


## 바텀업 다이나믹 프로그래밍으로 해결한 피보나치 수열
d = [0] * 100
# 첫번째 피보나치 수와 두번째 피보나치 수는 1
d[1] = 1
d[2] = 1
n = 99

# 피보나치 함수 반복문으로 구현(바텀업 다이나믹 프로그래밍)
for i in range(3, n+1):
    d[i] = d[i-1] + d[i-2]

print(d[n])

### 다이나믹 프로그래밍과 분할 정복
# 다이나믹 프로그래밍과 분할 정복은 모두 최적 부분 구조를 가질 때 사용할 수 있다.
# 다이나믹 프로그래밍과 분할 정복의 차이점은 부분 문제의 중복이다.
#   - 다이나믹 프로그래밍 문제에서는 각 부분 문제들이 서로 영향을 미치며 부분 문제가 중복된다.
#   - 분할 정복 문제에서는 동일한 부분 문제가 반복적으로 계산되지 않는다.
# 분할 정복의 대표적인 예시 : 퀵 정렬
# 퀵 정렬의 경우 Pivot 값이 자리를 변경해서 자리를 잡으면 기준 원소의 위치는 바뀌지 않는다.

## 접근 방법
# 주어진 문제가 다이나믹 프로그래밍 유형임을 파악하는 것이 중요하다.
# 가장 먼저 그리디, 구현, 완전 탐색 등의 아이디어로 문제를 해결할 수 있는 지 검토할 수 있다.
#   - 다른 알고리즘으로 풀이방법이 떠오르지 않거나, 시간복잡도가 매우 높은 경우 다이나믹 프로그래밍을 고려해본다,
# 일단 재귀 함수로 비효율적인 완전 탐색 프로그래밍을 작성한 뒤에 작은 문제에서 구한 답이 큰 문제에서 그대로 사용될 수 있다면 탑다운 방법을 사용해 코드를 개선하는 방법을 사용할 수 있다.
# 일반적인 코딩 테스트 수준에서는 기본 유형의 다이나믹 프로그래밍 문제가 출제되는 경우가 많다.