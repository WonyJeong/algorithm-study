#2231
import sys
input = sys.stdin.readline
def solved(N) :
    for i in range(1,N+1) :
        separatingNum = map(int,str(i))
        sumNum = i + sum(separatingNum) #하나의 정수와 그 정수를 이루는 낱개 수들의 합
        if(sumNum==N) : return i 
    return 0

if __name__ == '__main__':
    N = int(input().strip())
    print(solved(N))
