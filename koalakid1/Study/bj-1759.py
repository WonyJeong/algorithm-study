from itertools import combinations
from collections import deque
import sys

input = sys.stdin.readline

if __name__ == "__main__":
    l,c = map(int,input().strip().split())
    C = sorted(list(map(str,input().strip().split())))
    
    per = combinations(C,l)
    result = []
    checking = "aeiou"
    for i in per:
        checker = True
        checker2 = 0
        checker3 = 0
        queue = deque(list(i))
        first = queue.popleft()
        if first in checking:
            checker2 += 1
        else:
            checker3 += 1
        while queue:
            next = queue.popleft()
            if first[-1] < next:
                first += next
                if next in checking:
                    checker2 += 1
                else:
                    checker3 += 1
            else:
                checker = False
                break
        if checker and checker2 >= 1 and checker3 >= 2:
            result.append(first)
    
    for i in sorted(result):
        print(i)

            
