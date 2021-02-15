#1057
import sys
input = sys.stdin.readline


if __name__ == '__main__':
    N, Kim, Lim = map(int, input().strip().split())
    round_ = 0
    while Kim != Lim :
        Kim -= Kim//2
        Lim -= Lim//2
        round_ += 1

    print(round_)
