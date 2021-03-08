import sys
input = sys.stdin.readline

def dfs(start):
    if visit[start] == 1:
        return 0
    visit[start] = 1
    for i in s[start]:
        if d[i] == 0 or dfs(d[i]):
            d[i] = start
            return 1
    return 0




if __name__ == '__main__':
    n,m = map(int,input().split())
    task = [list(map(int,input().split()))[1:] for _ in range(n)]
    result=0
    visit= [-1]*(m+1)

    for i in range(n):
        check = [False] *(m+1)
        if dfs(n,m,task,i):
            result+=1

    print(result)

