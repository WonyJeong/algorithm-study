#2884
import sys
input = sys.stdin.readline
time = list(map(int,input().strip().split()))
if time[1] - 45 >= 0 : print(time[0], time[1]-45)
elif time[0]-1 >= 0 : print(time[0]-1, 60 + (time[1] - 45))
else : print(23, 60 + (time[1]-45))