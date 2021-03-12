import sys
input = sys.stdin.readline


if __name__ == "__main__":
    n, k = map(int, input().strip().split())

    if n <= k:
        print(0)
        sys.exit(0)

    result = 0
    while True:
        a = n
        b = 0
        while a:
            if a % 2:
                b += 1
            a //= 2

        if b <= k:
            print(result)
            sys.exit(0)

        result += 1
        n += 1
