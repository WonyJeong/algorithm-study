import sys

if __name__ == "__main__":
    input = sys.stdin.readline
    N = int(input())
    answer = "".join(input().strip().split())
    T = int(input())

    result = []
    for _ in range(T):
        other = "".join(input().strip().split())
        reverse = ""
        for i in other:
            if i == "1":
                reverse = "3" + reverse
            elif i == "2":
                reverse = "4" + reverse
            elif i == "3":
                reverse = "1" + reverse
            else:
                reverse = "2" + reverse
        count = 0
        while count < N:
            count += 1
            check = other[count:] + other[0:count]
            check2 = reverse[count:] + reverse[0:count]

            if check == answer or check2 == answer:
                result.append(other)
                break
    print(len(result))
    for i in result:
        for j in i:
            print(j, end=" ")
        print()
