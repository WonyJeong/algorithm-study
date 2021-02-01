#14681
import sys
input = sys.stdin.readline
x = int(input().strip())
y = int(input().strip())
if x > 0 and y > 0 : print(1)
elif x > 0 and y < 0 : print(4)
elif x < 0 and y > 0 : print(2)
else : print(3)