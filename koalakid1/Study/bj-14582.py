import sys

input = sys.stdin.readline


if __name__ == "__main__":
    inning = list(map(int, input().strip().split()))
    endOfInning = list(map(int, input().strip().split()))

    jeminis = 0
    startlink = 0

    win = False
    for i in range(9):
        jeminis += inning[i]
        if jeminis > startlink:
            win = True
        startlink += endOfInning[i]
        if jeminis < startlink:
            if win:
                print("Yes")
                break
    if win == False:
        print("No")
