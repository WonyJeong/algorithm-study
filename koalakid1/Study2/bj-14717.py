import sys

input = sys.stdin.readline

if __name__ == "__main__":
    a, b = map(int, input().strip().split())
    if a == b:
        answer = (143 + a) / 153
        print("%0.3f" % answer)
    else:
        count = 0
        s1 = (a + b) % 10
        for i in range(1, 11):
            for j in range(1, 11):
                s2 = (i+j) % 10
                if i != j and s1 > s2:
                    if i == a or i == b or j == a or j == b:
                        count += 1
                    else:
                        count += 2
        print(count)
        print("%0.3f" % (count / 153))
