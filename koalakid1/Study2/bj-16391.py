import sys
input = sys.stdin.readline
        

if __name__ == "__main__":
    n = int(input())
    bells = ""
    for _ in range(n):
        bells += input().strip()
    answer = 0
    bell = False
    while True:
        if bell:
            break

        a = bells.find("O")
        print(a,bells)
        if a == -1:
            bell = True
            break
        bells = "O" * a+ "Z" + bells[a+1:]
        answer += 1
    print(answer)