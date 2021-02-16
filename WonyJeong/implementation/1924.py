import sys

input = sys.stdin.readline


def getDay(x, y):
    d = ["SUN", "MON", "TUE", "WED", "THU", "FRI", "SAT"]
    m = [1, 4, 4, 0, 2, 5, 0, 3, 6, 1, 4, 6]

    print(d[abs(m[x - 1] + y - 1) % 7])


if __name__ == "__main__":
    x, y = map(int, input().strip().split())
    getDay(x, y)
