#1065
import sys
input = sys.stdin.readline
if __name__ == '__main__' :
    N = int(input().strip())
    count = 0 #한수 개수 세어줄 변수
    for num in range(1, N+1) :
        if num < 100 :
            count += 1
        else :
            number = list(map(int, str(num)))
            if number[2] - number[1] == number[1] - number[0] : count += 1
    print(count)
