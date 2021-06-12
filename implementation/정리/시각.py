n = int(input())
h = 0
s = 0
m = 0
count = 0
while True:
    s += 1
    if s == 60:
        s = 0
        m += 1
        if m == 60:
            m = 0
            h += 1
            if h > n:
                break
    if '3' in str(h)+str(m)+str(s):
        count += 1

print(count)


h = 0
s = 0
m = 0
count = 0

for i in range((n+1)*3600):
    h = i // 3600
    m = (i % 3600) // 60
    s = i % 60
    if '3' in str(h)+str(m)+str(s):
        count += 1

print(count)
