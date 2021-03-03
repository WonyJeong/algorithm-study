#1300
import sys
input = sys.stdin.readline

def solved(N,K):
    start = 1
    end = pow(N,2)
    step = 0

    while start <= end :
        mid = (start + end) // 2 
        step  += 1
        if K == mid :
            print(step * (step+1))
            break
        elif mid < K :
            start = mid + 1
        else :
            end = mid - 1

if __name__ == '__main__':
    N = int(input().strip())
    K = int(input().strip())
    solved(N,K)