# https://www.acmicpc.net/problem/1246
# 접근 방법
# 가격을 내림차순으로 정렬한 뒤 각 가격 당 얼마씩 수익을 얻을 수 있는지 체크하여 최대 수익이나는 가격과 수익을 출력한다.
n, m = map(int,input().split())
price = [int(input()) for _ in range(m)]
price.sort(reverse = True)
result = []
for i in range(m):
    result.append([price[i], price[i]*min(i+1, n)])
result.sort(key=lambda x:x[1], reverse=True)
print(result[0][0], result[0][1])