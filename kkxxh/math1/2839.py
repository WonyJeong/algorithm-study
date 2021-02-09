#2839
import sys

input = sys.stdin.readline
N = int(input())

three = 0 # 3킬로그램의 개수
five = 0  # 5킬로그램의 개수
temp = 0

if N % 5 == 0 :
    five = int( N // 5 )
    print(five)
elif N %  3 == 0 :
    three = int(N //3)
    print(three)
else :
    five = int(N // 5)
    temp =  N % 5
    while(1) :
        temp = temp % 3
        three += 1
        if temp % 3 == 0 : 
            print(five + three)
            break
        elif temp % 3 == 1 : 
            print(-1) 
            break
        elif temp % 3 == 2 : 
            print(-1)
            break
        