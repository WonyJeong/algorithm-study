#1330
import sys
input = sys.stdin.readline
A, B = map(int, input().strip().split())
if A > B: print(">")
elif A < B : print("<")
else: print("==")