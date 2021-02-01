#9498
import sys
input = sys.stdin.readline
score = int(input().strip())
if (score >= 90 and score <= 100) : print("A")
elif (score >= 80 and score < 90) : print("B")
elif (score >= 70 and score < 80) : print("C")
elif (score >= 60 and score < 70) : print("D")
else : print("F")