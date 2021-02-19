import sys
input = sys.stdin.readline

if __name__ == "__main__":
    n = input().strip()
    length = len(n)
    result = 0
    for i in range(length-1):
        result += int("9" + "0" * i) * (i+1)
    result += (int(n) - int("1" + "0" * (length - 1)) + 1) * length
    print(result)