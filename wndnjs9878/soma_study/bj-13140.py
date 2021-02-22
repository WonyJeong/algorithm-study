#13140
import sys
from itertools import permutations
input = sys.stdin.readline

def solution(N):
    number = [i for i in range(0,10)]
    for element in permutations(number,7):
        h, e, l, o, w ,r, d = element
        hello = h * 10000 + e * 1000 + l * 100 + l * 10 + o
        world = w * 10000 + o * 1000 + r * 100 + l * 10 + d
        if  h != 0 and w != 0 and hello + world == N :
            print(f"  {hello}")
            print(f"+ {world}")
            print("-------")
            if N >= 100000 :
                print(f" {N}")
            else :
                print(f"  {N}")
            return
    print("No Answer")


if __name__ == '__main__' :
    N = int(input().strip())
    solution(N)