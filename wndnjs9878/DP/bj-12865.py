import sys
input = sys.stdin.readline


# 2차원 배열
def solution(N,K,stuff):
    answer = [[0 for _ in range(K+1)] for _ in range(N)]

    for i in range(N):
        for j in range(1,K+1):
            weight = stuff[i][0] 
            value = stuff[i][1]
        
            if j < weight:
                answer[i][j] = answer[i - 1][j]
            else:
                answer[i][j] = max(answer[i - 1][j - weight] + value, answer[i - 1][j])

    # print(answer)
    return answer[N-1][K]


'''
1차원 배열  : 2차원 배열보다 메모리 크지만, 시간 빠름
def solution(N,K,stuff):
    answer = [0 for _ in range(K + 1)]
    for i in range(N):
        for j in range(K, stuff[i][0]-1, -1):
                answer[j] = max(answer[j], answer[j-stuff[i][0]] + stuff[i][1])
                
                
    return answer[K]

'''

if __name__ == '__main__':
    N, K = map(int, input().strip().split())
    stuff = []
    for _ in range(N):
        stuff.append(list(map(int, input().strip().split())))
    
    print(solution(N,K,stuff))