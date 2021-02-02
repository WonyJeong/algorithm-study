#2557
import sys

input = sys.stdin.readline
A = int(input().strip())
B = int(input().strip())
C = int(input().strip())
Arr = [0,0,0,0,0,0,0,0,0,0]
product = str(A * B * C) #숫자를 문자열로 변환

for i in range(len(product)) : 
    Arr[int(product[i])] += 1

for i in Arr :
    print(i)