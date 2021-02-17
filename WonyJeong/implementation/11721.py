import sys

input = sys.stdin.readline


if __name__ == "__main__":
    input_ = input().strip()
    length = len(input_)
    cursor = length // 10
    for i in range(0, cursor + 1):
        if i != cursor:
            print(input_[i * 10 : i * 10 + 10])
        else:
            print(input_[i * 10 : length])
