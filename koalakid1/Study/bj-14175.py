import sys

input = sys.stdin.readline


if __name__ == "__main__":
    M, N, K = map(int, input().strip().split())
    MN = [input().strip() for _ in range(M)]
    for i in MN:
        i = i.replace("X.", "X .").replace(".X", ". X").split()
        p = ""
        for j in i:
            p += j * K
        for i in range(K):
            print(p)
