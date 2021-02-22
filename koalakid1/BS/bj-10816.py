from collections import deque
import sys

input = sys.stdin.readline

if __name__ == "__main__":
    n = int(input())
    num1 = list(map(int,input().strip().split()))
    m = int(input())
    num2 = list(map(int,input().strip().split()))

    card = {}
    for i in num1:
        if i not in card:
            card[i] = 1
        else:
            card[i] += 1
    
    for i in num2:
        if i in card:
            print(card[i],end=" ")
        else:
            print(0,end=" ")