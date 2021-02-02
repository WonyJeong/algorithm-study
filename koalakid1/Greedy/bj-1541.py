import sys
input = sys.stdin.readline

string = input().strip()

strings = string.replace('-', ' - ').replace('+', ' + ').split()

number = list(map(int, string.replace("-", "+").split("+")))
result = 0
keeper = 0
minus = False
for i in range(len(number)):
    if i == len(number)-1:
        if minus:
            result -= number[i]
        else:
            if minus or keeper != 0:
                keeper += number[i]
            else:
                result += number[i]
    elif strings[2*i+1] == "+":
        if minus or keeper != 0:
            keeper += number[i]
        else:
            result += number[i]
        minus = False
    else:
        if keeper == 0:
            if minus:
                result -= number[i]
            else:
                result += number[i]
        else:
            keeper += number[i]
            result -= keeper
            keeper = 0
        minus = True

print(result-keeper)
