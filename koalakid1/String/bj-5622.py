import sys

input = sys.stdin.readline

string = input().strip()

number = {}

for i in range(26):
    alpha = chr(i + ord('A'))
    if i <= 2:
        number[alpha] = 3
    elif i <= 5:
        number[alpha] = 4
    elif i <= 8:
        number[alpha] = 5
    elif i <= 11:
        number[alpha] = 6
    elif i <= 14:
        number[alpha] = 7
    elif i <= 18:
        number[alpha] = 8
    elif i <= 21:
        number[alpha] = 9
    elif i <= 25:
        number[alpha] = 10

result = 0
for i in string:
    result += number[i]
print(result)
