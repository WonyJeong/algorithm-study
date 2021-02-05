import sys

input = sys.stdin.readline


def rgbStreet(T):
    memo = list(map(int, input().strip().split()))
    for i in range(1, T):
        next_ = list(map(int, input().strip().split()))
        newMemo = []
        for j in range(0, len(next_)):
            temp = []
            for k in range(0, len(memo)):
                if j != k:
                    temp.append(next_[j] + memo[k])
            newMemo.append(min(temp))
        memo = newMemo
    print(min(memo))


if __name__ == "__main__":
    T = int(input().strip())
    rgbStreet(T)
