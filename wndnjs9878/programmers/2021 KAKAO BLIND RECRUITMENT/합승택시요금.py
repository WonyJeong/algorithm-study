import sys
input = sys.stdin.readline
INF = sys.maxsize

def solution(n,s,a,b,fares):
    dist = [[INF for _ in range(n + 1)] for _ in range(n + 1)]

    for v1, v2, cost in fares:
        dist[v1][v2] = cost
        dist[v2][v1] = cost

    for i in range(1, n + 1):
        for v1 in range(1, n + 1):
            for v2 in range(1, n + 1):
                if v1 == v2:
                    dist[v1][v2] = 0
                    continue
                
                #else로 처리하면 시간초과남
                if dist[v1][v2] > dist[v1][i] + dist[i][v2]:
                    dist[v1][v2] = dist[v1][i] + dist[i][v2]
                    
    answer = dist[s][a] + dist[s][b]
    for i in range(1, n + 1):
        answer = min(answer, dist[s][i] + dist[i][a] + dist[i][b])
        
    return answer

if __name__ == '__main__':
    n = 6
    s = 4
    a = 6
    b = 2
    fares = [[4, 1, 10], [3, 5, 24], [5, 6, 2], [3, 1, 41], [5, 1, 24], [4, 6, 50], [2, 4, 66], [2, 3, 22], [1, 6, 25]]
    print(solution(n,s,a,b,fares))