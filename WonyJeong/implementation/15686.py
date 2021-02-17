import sys
from itertools import combinations

input = sys.stdin.readline


def getDist(r1, c1, r2, c2):
    return abs(r1 - r2) + abs(c1 - c2)


def chickenStreet():
    answer = sys.maxsize

    for v in combinations(chicken, M):
        cityChickenDist = 0
        for r1, c1 in house:
            chickenDist = sys.maxsize
            for r2, c2 in v:
                temp = getDist(r1, c1, r2, c2)
                if chickenDist > temp:
                    chickenDist = temp
            cityChickenDist += chickenDist

        if answer > cityChickenDist:
            answer = cityChickenDist

    print(answer)


if __name__ == "__main__":
    global N, M, house, chicken
    N, M = map(int, input().strip().split())
    house = []
    chicken = []
    for i in range(N):
        row = list(map(int, input().strip().split()))
        for j in range(N):
            if row[j] == 1:
                house.append([i, j])
                continue
            if row[j] == 2:
                chicken.append([i, j])
                continue
    chickenStreet()