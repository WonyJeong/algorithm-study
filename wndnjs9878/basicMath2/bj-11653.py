#11653
import sys
input = sys.stdin.readline

def solution(N):
    soinsu = 2
    while N != 1:
        if N % soinsu == 0 :
            N //= soinsu
            print(soinsu)
        else:
            soinsu += 1

if __name__ == '__main__':
    N = int(input().strip())
    solution(N)
