#1300
import sys
input = sys.stdin.readline

def solved(N,K):
    start = 1
    end = K

    while start <= end :
        mid = (start + end) // 2 
        step = 0
        for i in range(1, N+1):
            step += min( mid // i, N )
        if step >= K : #이분탐색 실행   
            answer = mid
            end = mid - 1
        else :
            start = mid + 1

    print(answer)

if __name__ == '__main__':
    N = int(input().strip())
    K = int(input().strip())
    solved(N,K)