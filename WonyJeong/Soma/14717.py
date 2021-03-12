import sys

input = sys.stdin.readline


def solution(n, m):
    card = [2 for _ in range(11)]
    answer = [0 for _ in range(21)]
    card[n] -= 1
    card[m] -= 1

    my = (n + m) % 10 if n != m else 10 + n
    for i in range(1, 11):
        if card[i] > 0:
            card[i] -= 1
            for j in range(i, 11):
                if card[j] > 0:
                    if i == j:
                        answer[10 + i] += 1
                    else:
                        answer[(i + j) % 10] += (card[i] + 1) * card[j]
            card[i] += 1

    temp = 0
    for i in range(my):
        temp += answer[i]

    print("%0.3f" % (temp / 153))


if __name__ == "__main__":
    n, m = map(int, input().strip().split())
    solution(n, m)
