import sys

input = sys.stdin.readline


def play(N, D, x, y, game):
    answer = 0
    case = []
    for i in range(0, N):
        temp = ""
        ct = 0
        j = i
        while ct < D:
            temp += str(game[j % N])
            ct += 1
            j += 1
        case.append(int(temp))

    for i in range(0, len(case)):
        if x <= case[i] <= y:
            answer += 1
    print(answer)


if __name__ == "__main__":
    T = int(input().strip())
    for _ in range(T):
        N, D = map(int, input().strip().split())
        X = list(map(int, input().strip().split()))
        Y = list(map(int, input().strip().split()))
        x = 0
        y = 0
        for i in range(0, D):
            x += X[D - i - 1] * 10 ** i
            y += Y[D - i - 1] * 10 ** i

        game = list(map(int, input().strip().split()))

        play(N, D, x, y, game)
