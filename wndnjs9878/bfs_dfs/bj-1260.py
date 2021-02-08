#1206
import sys
input = sys.stdin.readline

if __name__ == '__main__':

    N, M, V = map(int, input().strip().split())
    '''
    N : 정점의 개수
    M : 간선의 개수
    V : 탐색을 시작할 정점
    '''
    vertices = [False for _ in range(N+1)]
    
    edges = [[False for _ in range(N+1)] for _ in range(N+1)]
       

    for _ in range(M):
        vertice1, vertice2 = map(int, input().strip().split())
        edges[vertice1][vertice2] = True
        edges[vertice2][vertice1] = True

    for elem in edges:
        print(elem)
    

    



