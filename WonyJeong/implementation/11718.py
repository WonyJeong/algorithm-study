import sys

input = sys.stdin.readline


if __name__ == "__main__":
    while True:
        input_ = input().strip()
        if input_:
            print(input_)
        else:
            exit(0)
