import sys

input = sys.stdin.readline


def game(l, r):
    if sum(l) >= sum(r):
        print("No")
        return
    flag = False
    lsum = 0
    rsum = 0
    for i in range(0, 18):
        # n회 초
        idx = i // 2
        if i % 2 == 0:
            lsum += l[idx]
        # n회 말
        else:
            rsum += r[idx]

        if lsum > rsum:
            flag = True
            print("Yes")
            return
    print("No")


if __name__ == "__main__":
    l = list(map(int, input().strip().split()))
    r = list(map(int, input().strip().split()))
    l_ = []
    r_ = [0]
    for i in range(0, 9):
        l_.append(l[i])
        l_.append(l[i])
        r_.append(r[i])
        r_.append(r[i])
    l_.append(l_[17])

    game(l, r)
