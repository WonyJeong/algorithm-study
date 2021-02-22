import sys

input = sys.stdin.readline

if __name__ == "__main__":
    dic = {}
    N = int(input().strip())
    card = list(map(int, input().strip().split()))
    for c in card:
        if not c in dic.keys():
            dic[c] = set()
            dic[c] = 0
        dic[c] += 1

    M = int(input().strip())
    temp = list(map(int, input().strip().split()))

    for t in temp:
        if not t in dic.keys():
            print(0, end=" ")
        else:
            print(dic[t], end=" ")
