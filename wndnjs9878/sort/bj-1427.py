#1427
import sys
input = sys.stdin.readline

if __name__ == '__main__':
    arr = list(map(int, input().strip()))
    arr.sort(reverse=True)
    for element in arr :
        print(element, end='')
