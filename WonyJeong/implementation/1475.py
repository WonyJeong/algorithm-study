import sys

input = sys.stdin.readline


if __name__ == "__main__":
    N = list(map(str, input().strip()))
    room = [0 for _ in range(9)]
    pack = [1, 1, 1, 1, 1, 1, 2, 1, 1]
    for i in range(len(N)):
        if N[i] == "9":
            room[6] += 1
        else:
            room[int(N[i])] += 1

    for i in range(1, 10):
        temp = [i for _ in range(9)]
        comp = [x * y for x, y in zip(temp, pack)]
        flag = False
        for j in range(9):
            if comp[j] < room[j]:
                flag = True
                break

        if flag == False:
            print(i)
            exit(0)
