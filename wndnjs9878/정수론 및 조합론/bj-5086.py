import sys
input = sys.stdin.readline


if __name__ == '__main__':
    while True:
        a, b = map(int, input().strip().split())
        if a == b :
            break
        else :
            if b % a == 0 :
                print("factor")
            elif a % b == 0 :
                print("multiple")
            else :
                print("neither")