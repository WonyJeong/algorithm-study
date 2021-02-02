#2908
import sys
input = sys.stdin.readline
def change(num):
    num = list(map(int, str(num)))
    changedNum = num[2]*100 + num[1]*10 + num[0]
    return changedNum

if __name__ == '__main__' :
    A ,B= input().strip().split()
    print(max(change(A), change(B)))