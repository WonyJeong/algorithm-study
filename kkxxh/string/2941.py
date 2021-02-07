#2941
import sys

input = sys.stdin.readline
str = input().strip()
Croatia = ['c=','c-','dz=','d-','lj','nj','s=','z=']
for i in Croatia:
     str= str.replace(i,'_')
#print(str)
print(len(str))


