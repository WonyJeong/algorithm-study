#11053
import sys
input = sys.stdin.readline

def solution(N,seq):
    answer = [1] * N
    for i in range(N):
        for j in range(i):
            if seq[j] < seq[i] :
                answer[i] = max(answer[i], answer[j]+1)


    return max(answer)

if __name__ == '__main__':
    N = int(input().strip())
    seq = list(map(int, input().strip().split()))   
    print(solution(N,seq))