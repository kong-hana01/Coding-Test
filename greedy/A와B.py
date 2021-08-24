# https://www.acmicpc.net/problem/12904
# 접근 방법
# S가 T가 될 수 있는지 확인하기 위해 T에서 현재 문자열의 형태를 보고 제일 뒤에 B가 있다면 이를 지우고 T를 뒤집어준다. 혹은 제일 뒤에 A가 있다면 이를 지워준다.
# S와 T가 같은 길이가 되었을 때 위의 동작을 멈추고 만약 둘이 같다면 1, 다르다면 0을 출력한다.
# 시간 복잡도: O(N**2)
s = [x for x in input()]
t = [x for x in input()]
while len(s) < len(t):
    if t[-1] == "A":
        t.pop()
    else:
        t.pop()
        t = t[::-1]
        
if s == t:
    print(1)
else:
    print(0)