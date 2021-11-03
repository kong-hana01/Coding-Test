# https://www.acmicpc.net/problem/9095
# 접근 방법
# n이 4이상일 때, 다음과 같이 식을 추론할 수 있다. an = (1 + an-1) + (2 + an-2) + (3 + an-3)
# n이 4이상일 때, n을 1, 2, 3의 합으로 나타내는 방법은 다음과 같이 표현할 수 있다. An = A(n-1)  + A(n-2) + A(n-3)
# 위의 일반항을 토대로 다이나믹 프로그래밍을 진행한다.
def find_count(n):
    if d[n]:
        return d[n]
    d[n] = find_count(n-1) + find_count(n-2) + find_count(n-3)
    return d[n]

d = [0 for _ in range(11)]
d[1] = 1
d[2] = 2
d[3] = 4
tc = int(input())
for _ in range(tc):
    n = int(input())
    print(find_count(n))