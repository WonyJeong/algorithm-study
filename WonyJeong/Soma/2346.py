import sys

input = sys.stdin.readline


def boom(N, ballons):
    history = [False for _ in range(N)]
    answer = []
    index = 0
    for i in range(N):
        print(history)

        history[index] = True
        answer.append(index)

        dist = ballons[index]

        direction = 1 if dist > 0 else -1
        # index = (index + ballons[index]) % N
        cursor = 0
        if i < N - 1:
            while cursor < abs(dist):
                index = (index + 1 * direction) % N
                if history[index] == False:
                    cursor += 1

    for val in answer:
        print(val + 1, end=" ")


if __name__ == "__main__":
    N = int(input().strip())
    ballons = list(map(int, input().strip().split()))
    boom(N, ballons)
