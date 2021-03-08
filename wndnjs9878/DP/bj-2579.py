#2579
import sys
input = sys.stdin.readline

def solution(N,stairs):
    if N >= 3:
        answer = []
        answer.append(stairs[0])
        answer.append(stairs[0]+stairs[1])
        answer.append(max(stairs[0]+stairs[2], stairs[1]+stairs[2]))

        for i in range(3,N):
            answer.append(max(stairs[i] + stairs[i-1] + answer[i-3], stairs[i] + answer[i-2]))
        
        return answer[-1]
    elif N == 2:
        return stairs[0]+stairs[1]
    elif N == 1 :
        return stairs[0]

if __name__ == '__main__':
    N = int(input().strip())
    stairs = []
    for _ in range(N):
        stairs.append(int(input().strip()))
    print(solution(N,stairs))