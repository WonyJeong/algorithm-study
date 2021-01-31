import sys

input = sys.stdin.readline


def wordChecker(word):
    arr = []
    for i in range(0, 26):
        arr.append(False)

    if len(word) == 1:
        return 1

    cursor = 0
    while cursor < len(word):
        current = ord(word[cursor]) - 97
        if cursor == len(word) - 1:
            if arr[current] == True:
                return 0
            else:
                return 1

        next = ord(word[cursor + 1]) - 97

        if current != next:
            if arr[current] == False:
                arr[current] = True
            else:
                return 0
        cursor += 1

    return 1


if __name__ == "__main__":
    answer = 0

    N = int(input().strip())

    for _ in range(0, N):
        word = input().strip()
        answer += wordChecker(word)
        print("word : ", answer)
