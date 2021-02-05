import sys


if __name__ == "__main__":
    input = sys.stdin.readline
    N, M = map(int, input().strip().split())
    dh = set([input().strip() for i in range(N)])
    bh = set([input().strip() for i in range(M)])
    dbh = sorted(list(dh & bh))
    print(len(dbh))
    for i in dbh:
        print(i)
