#9498
import sys

input = sys.stdin.readline
a = int(input().strip())
if a>=90 : print("A")
elif a>=80 : print("B")
elif a>=70 : print("C")
elif a>=60 : print("D")
else : print("F")