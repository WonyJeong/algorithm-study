#1504
import sys
input = sys.stdin.readline


if __name__ == '__main__':
    N, E = map(int, input().strip().split())

    for _ in range(E):
        a, b, distance = map(int, input().strip().split())
        graph[a].append((b, distance))
    
    mustPassVertice1, mustPassVertice2 = map(int, input().strip().split())
    