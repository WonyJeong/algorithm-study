import sys

input = sys.stdin.readline


if __name__ == "__main__":
    while True:
        try:
            input_ = input().strip()
            print(input_)
        except:
            exit(0)
