import sys
input = sys.stdin.readline

if __name__ == "__main__":
    r,c = map(str,input().strip().split())
    for i in range(len(r)):
        c_index = c.find(r[i])
        if c_index != -1:
            r_index = i
            break
    
    for i in range(len(c)):
        if i != c_index:
            print('.' * r_index + c[i] + '.' * (len(r)-r_index-1))
        else:
            print(r)