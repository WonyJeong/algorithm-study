#1463
import sys
input = sys.stdin.readline

def solution(N):
    answer = [0 for _ in range(N+1)]
    for i in range(2, N+1):
        answer[i] = answer[i-1] +1
        if i % 2 == 0 :
            if answer[i] > answer[i//2] +1 :
                answer[i] = answer[i//2] + 1
        if i % 3 == 0 :
            if answer[i] > answer[i//3]+1:
                answer[i] = answer[i//3] +1

    return answer[-1]


if __name__ == '__main__':
    N = int(input().strip())
    print(solution(N))