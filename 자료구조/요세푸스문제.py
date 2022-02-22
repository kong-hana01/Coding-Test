# https://www.acmicpc.net/problem/1158
# 접근 방법
# 리스트에 1번 ~ n번까지의 값을 입력한 뒤에 인덱스를 더해가며 해당 인덱스의 값을 pop하고, 오세푸스 순열에 값을 추가한다.
# 이후 요세푸스 순열의 값을 출력한다.
n, k = map(int,input().split())
circle = [i for i in range(1, n+1)]
JosephusPermutation = []
i = k - 1
while circle:
    JosephusPermutation.append(str(circle.pop(i)))
    i += k - 1
    i %= len(circle) if circle else 1
print('<', ', '.join(JosephusPermutation), '>', sep='')