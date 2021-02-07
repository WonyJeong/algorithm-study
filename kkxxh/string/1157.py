#1157
import sys

input = sys.stdin.readline
S = input().strip() #대소문자로 이루어진 단어
temp = S.upper() #S를 대문자로 바꾸고 저장
Arr = []
max = 0
index = 0
for i in range(0, 91):
    Arr.append(0)
for i in range(0, len(temp)):
    Arr[ord(temp[i])] += 1
for i in range(65,91):
    if max < Arr[i] : 
        max = Arr[i]
        index = i
    elif max == Arr[i]:
        index = -1

if index != -1 :
     print(chr(index))
else : print("?")

