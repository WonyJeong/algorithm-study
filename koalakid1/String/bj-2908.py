import sys

input = sys.stdin.readline

a, b = list(map(str, input().strip().split()))


def reverseString(a):
    result = ""
    for i in a:
        result = i + result
    return int(result)


a = reverseString(a)
b = reverseString(b)

print(max(a, b))
