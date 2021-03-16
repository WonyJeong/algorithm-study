import sys
input = sys.stdin.readline
        

if __name__ == "__main__":
    n = int(input())
    
    S = set()

    for _ in range(n):
        temp = input().strip().split()
        if len(temp) == 1:
            if temp[0] == "all":
                S = set([i for i in range(1,21)])
            else:
                S = set()
        else:
            a,b = temp
            b = int(b)
            if a == "add":
                S.add(b)
            elif a == "remove":
                S.discard(b)
            elif a == "check":
                if b in S:
                    print(1)
                else:
                    print(0)
            elif a == "toggle":
                if b in S:
                    S.remove(b)
                else:
                    S.add(b)
