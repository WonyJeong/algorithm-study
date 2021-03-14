import sys
import math
input = sys.stdin.readline
        

if __name__ == "__main__":
    string = input().strip()
    x = string.find("x")
    if x == -1:
        if string != "0":
            if string == "1":
                print("x+W")
            elif string == "-1":
                print("-x+W")
            else:
                print(string + "x+W")
        else:
            print("W")
        sys.exit(0)
    num1 = int(string[:x]) // 2
    xx = str(num1) + "xx" if abs(num1) != 1 else "xx" if num1 == 1 else "-xx"
    if x != len(string)-1:
        oper = string[x+1]
        num2 = string[x+2:]
        
        x = "x" if num2 == "1" else num2 + "x" if num2 != "0" else ""
        if x:
            print(xx + oper + x + "+W")
        else:
            print(xx + "+W")
    else:
        print(xx+"+W")