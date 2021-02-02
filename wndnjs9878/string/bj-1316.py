#1316
import sys
input = sys.stdin.readline
if __name__ == '__main__' :
    N = int(input().strip())
    for _ in range(0, N):
        word = input().strip()
        for i in range(1, len(word)):
            if word.find(word[i-1]) > word.find(word[i]):
                N -= 1
                break
    print(N)

