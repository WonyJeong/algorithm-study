import sys
input = sys.stdin.readline

if __name__ == "__main__":
    N, kim, im = map(int, input().strip().split())
    count = 0
    while kim != im:
        kim -= kim//2
        im -= im//2
        count += 1
    print(count)
