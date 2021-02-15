#9461
import sys
input = sys.stdin.readline

if __name__ == '__main__':
    T = int(input().strip())
    for _ in range(T):
        P = [1,1,1]
        '''
        P[0] = 1
        P[1] = 1
        P[2] = 1
        P[N] = P[N-3] + P[N-2]
        '''
        N = int(input().strip())
        for i in range(3,N):
            P.append(P[i-3]+P[i-2])
        
        print(P[N-1])