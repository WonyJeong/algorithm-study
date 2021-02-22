import sys
from itertools import combinations

input = sys.stdin.readline

# a : 97, e : 101, i: 105, o : 111,  u :117
def solution(L, C, arr):
    answer = []
    arr = [ord(ch) for ch in arr]
    collection = [97, 101, 105, 111, 117]
    cons = []
    coll = []

    for i in range(len(arr)):
        if arr[i] in collection:
            coll.append(arr[i])
        else:
            cons.append(arr[i])

    cons.sort()
    coll.sort()

    for i in range(1, L):
        if L - i < 2:
            break
        for coll_ in combinations(coll, i):
            for cons_ in combinations(cons, L - i):
                temp = list(coll_) + list(cons_)
                temp = sorted(temp)
                s = ""
                for c in temp:
                    s += chr(c)
                answer.append(s)

    print("\n".join(sorted(answer)))


if __name__ == "__main__":
    L, C = map(int, input().strip().split())
    solution(L, C, list(map(str, input().strip().split())))
