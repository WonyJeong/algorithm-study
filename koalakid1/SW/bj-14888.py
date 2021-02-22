from itertools import permutations
from collections import deque
import sys

input = sys.stdin.readline

if __name__ == "__main__":
    n = int(input())
    a = list(map(int,input().strip().split()))
    o1,o2,o3,o4 = list(map(int,input().strip().split()))

    operations = []
    operations.extend(["+"] * o1 + ["-"] * o2 + ["*"] * o3 + ["//"] * o4)
    
    per = permutations(operations,n-1)

    _max = -1000000000
    _min = 1000000000

    for i in per:
        queue = deque(a)
        index = 0
        result = queue.popleft()
        while queue:
            operation = i[index]
            num = queue.popleft()
            index += 1
            if operation == "+":
                result += num
            elif operation == "-":
                result -= num
            elif operation == "*":
                result *= num
            else:
                if result < 0:
                    result = -result
                    result //= num
                    result = -result
                else:
                    result //= num
        _max = max(_max, result)
        _min = min(_min, result)
    
    print(_max)
    print(_min)
            
