import sys
from itertools import combinations
        

if __name__ == "__main__":
    while True:
        s = input()
        if s == '.':
            break
        strings = []
        temp = True
        for i in s:
            if i == "(" or i == "[":
                strings.append(i)
            elif i == ")":
                if not strings or strings[-1] == "[":
                    temp = False
                    break
                elif strings[-1] == "(":
                    strings.pop()
            elif i == "]":
                if not strings or strings[-1] == "(":
                    temp = False
                    break
                elif strings[-1] == "[":
                    strings.pop()
        if temp and not strings:
            print("yes")
        else:
            print("no")