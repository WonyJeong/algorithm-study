import sys
import math

input = sys.stdin.readline
max_ = sys.maxsize * -1
min_ = sys.maxsize


def recursive(cum, i, plus, minus, mul, div):
    global max_, min_
    if i == N:
        if cum > max_:
            max_ = cum
        if cum < min_:
            min_ = cum
        return

    i += 1
    if plus > 0:
        recursive(cum + nums[i], i, plus - 1, minus, mul, div)
    if minus > 0:
        recursive(cum - nums[i], i, plus, minus - 1, mul, div)
    if mul > 0:
        recursive(cum * nums[i], i, plus, minus, mul - 1, div)
    if div > 0:
        temp = cum / nums[i]
        if temp < 0:
            temp = math.floor(abs(temp)) * -1
        else:
            temp = math.floor(temp)
        recursive(temp, i, plus, minus, mul, div - 1)

    if plus == 0 and minus == 0 and mul == 0 and div == 0:
        recursive(cum, N, 0, 0, 0, 0)


def solution(N, nums, oper):
    global max_, min_
    recursive(nums[0], 0, oper[0], oper[1], oper[2], oper[3])

    print(max_)
    print(min_)


if __name__ == "__main__":
    N = int(input().strip())
    nums = list(map(int, input().strip().split()))
    oper = list(map(int, input().strip().split()))
    solution(N, nums, oper)