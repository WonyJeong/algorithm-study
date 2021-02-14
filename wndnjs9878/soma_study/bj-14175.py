#14175
import sys
input = sys.stdin.readline

if __name__ == '__main__' :
    M, N, K = map(int, input().strip().split())
    paper = [list(input().strip()) for _ in range(M)]

    # from pprint import pprint
    # pprint(paper)
    for row in paper:
        for _ in range(K):
            for i in range(len(row)) :
                if row[i] == 'X' :
                    print('X'*K, end='')
                else :
                    print('.'*K, end='')
            print()

