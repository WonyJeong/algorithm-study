import sys
input = sys.stdin.readline
        

if __name__ == "__main__":
    x = int(input())
    answer = 0
    while x > 0:
        answer += x % 2
        x //= 2
    print(answer)