# https://www.acmicpc.net/problem/1269
import sys
input = sys.stdin.readline
n, m = map(int, input().split())
a = set(input().split())
b = set(input().split())
print(len((a - b) | (b - a)))