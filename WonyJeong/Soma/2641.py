import sys

input = sys.stdin.readline


def findSameShape():
    global shape
    global rshape

    T = int(input().strip())
    answer = []
    for _ in range(T):
        temp = list(map(str, input().strip().split()))
        shape_ = "".join(temp)

        if shape_ in shape:
            answer.append(temp)
            continue

        if shape_ in rshape:
            answer.append(temp)
            continue

    print(len(answer))
    for i in range(0, len(answer)):
        print(" ".join(answer[i]))


if __name__ == "__main__":
    L = int(input().strip())
    temp = list(map(str, input().strip().split()))
    rshape_ = []
    for i in range(0, len(temp)):
        if temp[i] == "1":
            rshape_.append("3")
        elif temp[i] == "2":
            rshape_.append("4")
        elif temp[i] == "3":
            rshape_.append("1")
        elif temp[i] == "4":
            rshape_.append("2")

    rshape_.reverse()
    shape = "".join(temp)
    rshape = "".join(rshape_)

    shape += shape
    rshape += rshape

    findSameShape()