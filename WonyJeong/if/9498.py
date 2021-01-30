import sys
input = sys.stdin.readline

grade = int(input().strip())
if grade >= 90 :
    print("A")
elif grade >= 80 :
    print("B")
elif grade >= 70 :
    print("C")
elif grade >= 60 :
    print("D")
else:
    print("F")
