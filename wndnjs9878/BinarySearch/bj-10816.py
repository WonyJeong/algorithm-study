import sys
input = sys.stdin.readline

def solved(N, card, M, sanggeun):
    card_count = {}
    for num in card :
        if num in card_count :
            card_count[num] += 1
        else :
            card_count[num] = 1

    for sang in sanggeun:
        if sang in card_count:
            print(card_count[sang], end=" ")
        else:
            print(0, end=" ")

if __name__ == '__main__':
    N = int(input().strip())
    card = list(map(int, input().strip().split()))
    M = int(input().strip())
    sanggeun = list(map(int, input().strip().split()))

    solved(N,card,M,sanggeun)