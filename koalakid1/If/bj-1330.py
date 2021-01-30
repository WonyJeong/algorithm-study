import sys

input = sys.stdin.readline

n, m = map(int, input().strip().split())

print(n == m and "==" or n < m and "<" or ">")
