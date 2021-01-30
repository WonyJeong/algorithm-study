import sys

input = sys.stdin.readline

num = int(input())

result = 0
for _ in range(num):

    string = input().strip()
    alpha = [0 for _ in range(26)]

    count = 0
    prev = ""
    for i in string:
        count += 1
        index = ord(i) - ord('a')
        if prev != i:
            count = 1
            prev = i
        if alpha[index] < count:
            alpha[index] = count
        else:
            result -= 1
            break
    result += 1
print(result)
