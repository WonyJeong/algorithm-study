# 2447
import sys
input = sys.stdin.readline

'''
*********
* ** ** *
*********
***   ***
* *   * *
***   ***
*********
* ** ** *
*********
'''


def star(pattern):
    star = []
    for i in range(3*len(pattern)):
        if i // len(pattern) == 1:
            star.append(pattern[i%len(pattern)]+""+len(pattern)+pattern[i%len(pattern)])
        else:
            star.append(pattern[i%len(pattern)]*3)
    return list(star)


if __name__ == '__main__':
    N = int(input().strip())
    pattern = ['***', '* *', '***']
    count = 0
    while N != 3:
        N = N // 3
        count += 1

    for _ in range(count):
        pattern = star(pattern)
    
    for p in pattern:
        print(p)
