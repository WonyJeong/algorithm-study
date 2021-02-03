import sys
from itertools import permutations

input = sys.stdin.readline


def hello_world(N):
    if N > 190000:
        print("No Answer")
        return

    h = 10000
    e = 1000
    l = 120
    o = 1001
    w = 10000
    r = 100
    d = 1

    hello = [h, e, l, o, w, r, d]
    nums = [0, 1, 2, 3, 4, 5, 6, 7, 8, 9]

    for comb_ in permutations(nums, 7):
        comb = list(comb_)
        if comb[0] != 0 and comb[4] != 0:
            if sum([i * j for i, j in zip(hello, comb)]) == N:

                print(f"  {comb[0]}{comb[1]}{comb[2]}{comb[2]}{comb[3]}")
                print(f"+ {comb[4]}{comb[3]}{comb[5]}{comb[2]}{comb[6]}")
                print("-------")
                if N >= 100000:
                    print(f" {N}")
                else:
                    print(f"  {N}")
                return

    print("No Answer")


if __name__ == "__main__":
    N = int(input().strip())
    hello_world(N)