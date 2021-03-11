#1912
import sys
input = sys.stdin.readline

def solution(N,seq):
    answer = [0 for _ in range(N)]
    answer[0] = seq[0]

    for i in range(1,N):
        if answer[i-1] + seq[i] >= seq[i] :
            answer[i] = answer[i-1] + seq[i]
        else :
            answer[i] = seq[i]

    #print(answer)
    return max(answer)


if __name__ == '__main__':
    N = int(input().strip())
    seq = list(map(int, input().strip().split()))
    print(solution(N,seq))