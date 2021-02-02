import sys

input = sys.stdin.readline


def getTime(T, time):
    answer = 0
    time = sorted(time)
    for i in range(0, T):
        answer += (T - i) * time[i]
    print(answer)


if __name__ == "__main__":
    T = int(input().strip())
    time = list(map(int, input().strip().split()))
    getTime(T, time)
