#2775
import sys
input = sys.stdin.readline

def solved(k,n):
    '''
    k : 층
    n : 호
    '''
    numberOfResidents = [ i for i in range(1, n+1)] #호수에 대한 누적값
    for _ in range(k):
        for i in range(1,n):
            numberOfResidents[i] += numberOfResidents[i-1]
    return numberOfResidents[-1]


if __name__ == '__main__':
    T = int(input().strip())
    for _ in range(0, T):
        k = int(input().strip())
        n = int(input().strip())
        print(solved(k,n))
        