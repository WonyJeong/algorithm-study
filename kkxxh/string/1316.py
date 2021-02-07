#1316
import sys

def checker(str):
    for i in range(1, len(str)):
        if str.find(str[i]) < str.find(str[i-1]):
            return False

input = sys.stdin.readline
N = int(input().strip())
count = N
for i in range(0,N):
    str = input().strip()
    if checker(str) == False :
        count -= 1

print(count)