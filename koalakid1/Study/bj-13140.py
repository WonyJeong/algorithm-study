import sys
import itertools

if __name__ == "__main__":
    number = [0, 1, 2, 3, 4, 5, 6, 7, 8, 9]
    N = int(input())
    result = True
    for d, e, h, l, o, r, w in itertools.permutations(number, 7):
        hello = 10000 * h + 1000 * e + 100 * l + 10 * l + o
        world = 10000 * w + 1000 * o + 100 * r + 10 * l + d
        answer = hello + world
        if answer == N and h != 0 and w != 0:
            print(f"  {hello}")
            print(f"+ {world}")
            print("-------")
            print(N >= 100000 and f" {N}" or f"  {N}")
            result = False
            break
    if result:
        print("No Answer")
