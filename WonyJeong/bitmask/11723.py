import sys

input = sys.stdin.readline

size = 10
1 2 3 4 5 6 7 8 9 10
0 0 1 0 0 0 0 0 0 1 

00000000000000001

value + 1 % 2



def solution(N):
    init = set()
    mset = set()
    for i in range(1, 21):
        init.add(i)

    for _ in range(N):
        comand = input().strip().split()
        if len(comand) > 1:
            num = int(comand[1])
        if comand[0] == "add":
            mset.add(num)
        elif comand[0][0] == "r":
            mset.discard(num)
        elif comand[0][0] == "c":
            if num in mset:
                print(1)
            else:
                print(0)
        elif comand[0][0] == "t":
            if num in mset:
                mset.discard(num)
            else:
                mset.add(num)
        elif comand[0][0] == "a":
            mset = init
        elif comand[0][0] == "e":
            mset = set()


if __name__ == "__main__":
    solution(int(input().strip()))
