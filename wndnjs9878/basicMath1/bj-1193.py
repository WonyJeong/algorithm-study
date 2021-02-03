#1193
import sys
input = sys.stdin.readline

def solved(N) :
    cycle = 1 #number of Cycle
    count = 0 #comparing with N
    while True :
        count += cycle
        if count-cycle < N and N <= count :
            evenTop = cycle - (count - N)
            oddTop = count - N + 1
            if cycle % 2 == 0 :
                return f'{evenTop}/{oddTop}'
            else :
                return f'{oddTop}/{evenTop}'
        cycle += 1
    
if __name__ =='__main__':
    N = int(input().strip())
    print(solved(N))
