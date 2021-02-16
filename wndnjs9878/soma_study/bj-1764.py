#1764
import sys
input = sys.stdin.readline


if __name__ == '__main__':
    N, M = map(int, input().strip().split())
    noListen = set([input().strip() for _ in range(N)])
    noSee = set([input().strip() for _ in range(M)])
    noListenAndSee = noListen & noSee

    print(len(noListenAndSee))
    result = sorted(list(noListenAndSee))
    for element in result:
        print(element)