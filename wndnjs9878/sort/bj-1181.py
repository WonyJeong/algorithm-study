#1181
import sys
input = sys.stdin.readline

if __name__ == '__main__':
    N = int(input().strip())
    arr = [ '0' for _ in range(N)]
    for i in range(N):
        arr[i] = (input().strip())
     
    nonrepeatArr = list(set(arr))
    nonrepeatArr.sort()

    nonrepeatArr = sorted(nonrepeatArr, key=lambda x:len(x))
    for element in nonrepeatArr :
        print(element)