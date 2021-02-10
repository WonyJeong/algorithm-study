#1193 분수찾기
import sys

input = sys.stdin.readline
N = int(input())

number = 1
while N > number:
    N -= number
    number += 1

if number %2 == 0 :
    top = N
    bottom = number - N + 1
else:
    top = number - N + 1
    bottom = N
    
print(top, '/', bottom)
