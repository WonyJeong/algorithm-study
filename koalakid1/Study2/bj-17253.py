import sys
import math
input = sys.stdin.readline
        

if __name__ == "__main__":
    n = int(input())
    if n == 0:
        print("NO")
        sys.exit(0)
    while n:
        if n % 3 > 1:
            print("NO")
            sys.exit(0)
        n //= 3
    print("YES")    

