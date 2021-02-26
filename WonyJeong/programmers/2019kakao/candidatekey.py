import sys
from itertools import combinations

input = sys.stdin.readline


def solution(relation):
    answer = 0
    result = []
    col = len(relation[0])
    row = len(relation)
    checked = [col + 1 for i in range(0, col)]

    for i in range(1, col + 1):
        for comb in combinations(range(col), i):
            flag = True
            skipThisComb = False
            comb = list(comb)
            tup = []
            for j in range(0, row):
                temp = []
                for k in range(0, len(comb)):
                    temp.append(relation[j][comb[k]])
                tup.append(tuple(temp))
            tupLen = len(tup)
            tup = set(tup)
            if len(tup) == tupLen:
                result.append(comb)

    result2 = [[i, False] for i in result]
    for i in range(0, len(result2) - 1):
        if result2[i][1] == False:
            a = result2[i][0]
            lena = len(a)
            for j in range(i + 1, len(result2)):
                intersec = set(a).intersection(set(result2[j][0]))
                if len(intersec) == lena:
                    result2[j][1] = True

    for arr, bool_ in result2:
        if bool_ == False:
            answer += 1
    return answer


if __name__ == "__main__":
    print(
        solution(
            [
                ["100", "ryan", "music", "2"],
                ["200", "apeach", "math", "2"],
                ["300", "tube", "computer", "3"],
                ["400", "con", "computer", "4"],
                ["500", "muzi", "music", "3"],
                ["600", "apeach", "music", "2"],
            ]
        )
    )
