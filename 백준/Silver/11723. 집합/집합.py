# https://www.acmicpc.net/problem/11723

def add(s, x):
    s = s | (1 << x-1)
    return s

def remove(s, x):
    s = s & ~(1 << x-1)
    return s

def check(s, x):
    if len(bin(s)[2:]) >= x:
        return bin(s)[2:][-x]
    return 0

def toggle(s, x):
    s = s ^ (1 << x-1)
    return s

def all(s):
    for i in range(20):
        s = s | (1 << i)
    return s

def empty(s):
    s = 0
    return s

import sys
input = sys.stdin.readline
m = int(input())
s = 0
for i in range(m):
    command = input().split()
    if command[0] == "add":
        s = add(s, int(command[1]))
    elif command[0] == "remove":
        s = remove(s, int(command[1]))
    elif command[0] == "check":
        print(check(s, int(command[1])))
    elif command[0] == "toggle":
        s = toggle(s, int(command[1]))
    elif command[0] == "all":
        s = all(s)
    else:
        s = empty(s)
    