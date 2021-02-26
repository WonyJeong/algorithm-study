#1806
import sys
input = sys.stdin.readline

def solved(N, S, seq):
    answer = sys.maxsize
    left = 0
    right = left + 2
    seq = sorted(seq)
    count = 0

    while sum(seq[left:right]) <= S :
        
        tmp = sum(seq[left:right])
        if tmp < S :
            right += 1
        else :
            print(left, right)
            count += 1
            print(count)    
            answer = min(answer, right-left)
            left += 1
            right = left + 2
    
    
    print(answer)

if __name__ == '__main__':
    N, S = map(int, input().strip().split())
    seq = list(map(int, input().strip().split()))
    solved(N, S, seq)