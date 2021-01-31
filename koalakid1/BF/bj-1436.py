import sys

input = sys.stdin.readline

num = int(input())

count = 0
sixsixsix = 666
while True:
    if '666' in str(sixsixsix):
        count += 1
    if count == num:
        print(sixsixsix)
        break
    sixsixsix += 1
