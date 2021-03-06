#11404
import sys
INF = sys.maxsize
input = sys.stdin.readline

def solution(n,m,bus_info):
    dist = [[INF for _ in range(n + 1)] for _ in range(n + 1)]

    for info in bus_info:
        dist[info[0]][info[1]] = min(info[2], dist[info[0]][info[1]])

    for i in range(1, n + 1):
        for v1 in range(1, n + 1):
            for v2 in range(1, n + 1):
                if v1 == v2:
                    dist[v1][v2] = 0
                    continue
                
                else:
                    dist[v1][v2] = min(dist[v1][v2],dist[v1][i] + dist[i][v2])
    
    for i in range(1,n+1):
        for j in range(1,n+1):
            if dist[i][j]==INF:
                print(0,end=' ')
            else:
                print(dist[i][j],end=' ')
        print()




if __name__ == '__main__':
    n = int(input().strip())
    m = int(input().strip())
    bus_info = [ list(map(int, input().strip().split())) for _ in range(m) ]
    solution(n,m,bus_info)