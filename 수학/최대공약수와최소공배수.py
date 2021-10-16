n, m = map(int, input().split())

def gcd(n, m):
    # n이 m보다 클 때에만 나머지가 0이상 나온다.
    # m이 n보다 큰 경우 나머지는 무조건 0이 나온다.
    if n < m:
        n, m = m, n 
    if n % m == 0:
        return m
    return gcd(m, n % m)
    
def lcm(n, m):
    return n * m // gcd(n,m)

print(gcd(n, m))
print(lcm(n, m))
