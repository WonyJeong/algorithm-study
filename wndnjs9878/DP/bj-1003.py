#1003
import sys
input = sys.stdin.readline
    
if __name__ == '__main__':
    T = int(input().strip())
    for _ in range(T):
        N = int(input().strip())
        zero = 1
        one = 0
        temp = 0
        for _ in range(N):
            temp = one
            one += zero
            zero = temp
        print(zero, one)
        