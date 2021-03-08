import sys

input = sys.stdin.readline


def solution(n, arr1, arr2):
    answer = []
    map_ = []
    for arr in [arr1, arr2]:
        map__ = []
        for val in arr:
            temp = []
            while val != 0:
                temp.append(val % 2)
                val = val // 2
            while len(temp) != n:
                temp.append(0)
            temp.reverse()
            map__.append(temp)
        map_.append(map__)

    for row1, row2 in zip(map_[0], map_[1]):
        temp = ""
        for i, j in zip(row1, row2):
            temp += "#" if i or j else " "

        answer.append(temp)

    return answer


if __name__ == "__main__":
    n = 5
    arr1 = [9, 20, 28, 18, 11]
    arr2 = [30, 1, 21, 17, 28]
    print(solution(n, arr1, arr2))
