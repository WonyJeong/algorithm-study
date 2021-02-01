#1110
import sys
input = sys.stdin.readline
N = int(input().strip()) #97
origin = N
count = 0
while True :
    temp = int( ( int(N/10) + int(N%10) ) %10) # 9 + 7 = 16 -> 6
    # print(temp) # 6
    N = int(N%10*10) + temp  # 70 + 6 = 76
    # print(N)
    count += 1
    if N == origin : break

print(count)
