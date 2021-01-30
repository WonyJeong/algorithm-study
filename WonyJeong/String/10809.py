import sys

input = sys.stdin.readline

str = input().strip()

for i in range(97, 123):
    print(f"{str.find(chr(i))}", end=" ")
