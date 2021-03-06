#1149
import sys
input = sys.stdin.readline

def solution(N,home):
    answer = 0
    for i in range(1,N):
        home[i][0] = min(home[i-1][1],home[i-1][2]) + home[i][0]
        home[i][1] = min(home[i-1][0],home[i-1][2]) + home[i][1]
        home[i][2] = min(home[i-1][0],home[i-1][1]) + home[i][2]
    
    answer = min(home[N-1][0], home[N-1][1], home[N-1][2])

    return answer

if __name__ == '__main__':
    N = int(input().strip())
    home = [i for i in range(N)]
    for i in range(N):
        home[i] = list(map(int, input().strip().split()))

    print(solution(N, home))