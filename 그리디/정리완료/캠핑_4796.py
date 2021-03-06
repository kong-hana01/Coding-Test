# 캠핑장을 연속하는 P일 중, L일동안만 사용할 수 있다. 강산이는 이제 막 V일짜리 휴가를 시작했다. 강산이가 캠핑장을 최대 며칠동안 사용할 수 있을까? (1 < L < P < V)

# 접근 방법
# 연속하는 p일 중 L일 동안만 사용할 수 있을 때, 최대한 캠핑장을 사용하기 위해서는 주어진 V에서 연속하는 P일을 나누어 몫만큼 사용할 수 있는 L을 곱한 뒤, 나머지에 대해 따로 처리해주면 된다.
# 이때, 사용할 수 있는 L일과 나머지를 비교했을 때, 나머지가 더 크다면 L만큼 더하고, L이 더 크다면 나머지를 더한다.

i = 0
while True:
    l, p, v = map(int, input().split())
    i += 1
    # l, p, v가 모두 0일 때 종료
    if l == p == v == 0:
        break
    # 연속하는 P일 중 L일 동안만 사용할 수 있기 때문에 주어진 V일에 대해 P로 나눠주고 몫에 대해 이를 L만큼 곱해준다.
    count = ( v // p ) * l
    
    # 주어진 휴가기간과 p를 나눴을 때의 나머지가 사용할 수 있는 L보다 클 때 count에 L을 더한다.
    if v % p > l:
        count += l
    # 주어진 휴가기간과 p를 나눴을 때의 나머지가 사용할 수 있는 L보다 작을 때 count에 나머지를 더한다.
    elif v % p <= l:
        count += v % p
    print('Case {}:'.format(i), count)