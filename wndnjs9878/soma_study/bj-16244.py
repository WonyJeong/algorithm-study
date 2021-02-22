#16244
import sys
from itertools import combinations
input = sys.stdin.readline


if __name__ == '__main__':
    N = int(input().strip())
    enemies = list(map(int, input().strip().split()))

    last = sum(enemies) // 2
    lastenemy = enemies.pop(enemies.index(last))
    for element in enemies :
        print(element, end=" ")
    print(lastenemy)
