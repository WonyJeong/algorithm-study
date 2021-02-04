#10872
import sys
input = sys.stdin.readline
def solved(N):
    if N == 0 :
        return 1
    return N*solved(N-1)

if __name__ == '__main__':
    N = int(input().strip())
    print(solved(N))