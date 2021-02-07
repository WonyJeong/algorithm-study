#1436
import sys
input = sys.stdin.readline

def solution(N) :
    result = 0
    worldEnd = 666
    while True :
        if '666' in str(worldEnd) :
            result += 1
        if result == N:
            return worldEnd
        worldEnd += 1

if __name__ == '__main__':
    N = int(input().strip())
    print(solution(N))