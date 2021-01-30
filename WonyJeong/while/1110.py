import sys

input = sys.stdin.readline

cycle = 0

input_num = input().strip()

first_num = int(input_num)
result = input_num

while True:
    if int(result) < 10:
        result = "0" + str(int(result))

    l1 = result[0]
    l2 = result[1]
    r = int(l1) + int(l2)

    result = str(l2) + str(r % 10)

    cycle += 1
    if first_num == int(result):
        print(cycle)
        break
