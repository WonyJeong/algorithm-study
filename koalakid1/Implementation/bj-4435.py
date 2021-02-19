import sys
input = sys.stdin.readline

if __name__ == "__main__":
    T = int(input())
    g_p = [1, 2, 3, 3, 4, 10]
    s_p = [1, 2, 2, 2, 3, 5, 10]
    for count in range(1,T+1):
        g = list(map(int,input().strip().split()))
        s = list(map(int,input().strip().split()))
        g_a = 0
        s_a = 0
        for i in range(6):
            g_a += g[i] * g_p[i]
        
        for i in range(7):
            s_a += s[i] * s_p[i]
        
        print(f"Battle {count}: ", end= "")
        print(g_a > s_a and "Good triumphs over Evil" or g_a < s_a and "Evil eradicates all trace of Good" or "No victor on this battle field")