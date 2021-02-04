#2839
import sys
input = sys.stdin.readline
def solved(N) :
    if (N%5) == 0 :
        return N//5
    elif (N%5%3) == 0 :
        return (N//5 + N%5//3)
    else :
        numberOfFive = N//5
        i=1
        while numberOfFive-i > 0 :
            if (N - 5 * (numberOfFive-i)) % 3 == 0:
                return (numberOfFive-i) + (N - 5 * (numberOfFive-i)) // 3
            i += 1
            
    if (N%3) == 0 :
        return N//3
    return -1

if __name__ == '__main__':
    N = int(input().strip())
    print(solved(N))