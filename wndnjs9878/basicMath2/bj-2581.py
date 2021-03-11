#2581
import sys
input = sys.stdin.readline

def solution(M, N):
    answer = []
    for num in range(M, N+1):
        if num == 1 :
            continue
        if num == 2 :
            answer.append(num)
        for i in range(2,num):
            if num%i == 0:
                break
            elif i == num-1 and num%i != 0 :
                answer.append(num)
            else:
                continue
    if len(answer) == 0 :
        print(-1)
    else :
        print(sum(answer))
        print(min(answer))

if __name__ == '__main__':
    M = int(input().strip())
    N = int(input().strip())
    solution(M,N)
