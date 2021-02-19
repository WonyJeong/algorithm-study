import sys
input = sys.stdin.readline

if __name__ == "__main__":
    a = int(input())
    o = input().strip()
    b = int(input())
    print(o == "+" and a + b or a * b)