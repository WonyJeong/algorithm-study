#3053
import sys
import math
input = sys.stdin.readline

def solution(R):
    print('%.6f' %(math.pi*pow(R,2)))
    print('%.6f' %(2*R*R))


if __name__ == '__main__':
    R = int(input().strip())
    solution(R)