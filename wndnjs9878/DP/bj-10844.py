#10844
import sys
input = sys.stdin.readline

def solution(N):
    answer = []
    answer.append([1 for _ in range(10)])
    for _ in range(1,N):
        answer.append([0 for _ in range(10)])

    for i in range(1,N):
        for j in range(10):
            if j == 0:
                answer[i][j] = answer[i-1][j+1]
            elif j == 9:
                answer[i][j] = answer[i-1][j-1]
            else :
                answer[i][j] = answer[i-1][j-1] + answer[i-1][j+1]
                
    return  (sum(answer[-1])-answer[-1][0]) % 1000000000

if __name__ == '__main__':
    N = int(input().strip())
    print(solution(N))