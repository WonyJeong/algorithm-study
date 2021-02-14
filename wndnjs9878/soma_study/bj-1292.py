#1292
import sys
input = sys.stdin.readline


if __name__ == '__main__':
    A, B = map(int, input().strip().split())
    sequence = []
    count = 1
    while len(sequence) < B :
        for _ in range(0,count):
            sequence.append(count)
        count += 1
    # print(sequence)

    result = 0
    for i in range(B-A+1): #0~4
        result += sequence[A+i-1] #s[3]+s[4]+s[5]+s[6]+s[7]

    print(result)