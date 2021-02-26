#1806
import sys
input = sys.stdin.readline

def solved(N, S, seq):
    answer = sys.maxsize
    left = 0
    right = 0
    Sum = seq[left]
    while True :
        if Sum < S :
            right += 1
            if right == N :
                if answer == sys.maxsize:
                    return 0
                break
            Sum += seq[right]
        else:
            # print('log >>> ',left,right)
            answer = min(answer,right-left+1)
            Sum -= seq[left]
            left += 1
    return answer

if __name__ == '__main__':
    N, S = map(int, input().strip().split())
    seq = list(map(int, input().strip().split()))
    print(solved(N, S, seq))