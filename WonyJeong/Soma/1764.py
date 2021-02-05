import sys

input = sys.stdin.readline


def emeqhwkq(N2, dic):
    dbj = []
    for _ in range(N2):
        str_ = input().strip()
        if str_[0] in dic and str_ in dic[str_[0]]:
            dbj.append(str_)

    print(len(dbj))
    print("\n".join(sorted(dbj)))


if __name__ == "__main__":
    N1, N2 = map(int, input().strip().split())
    dic = {}
    for _ in range(0, N1):
        inputs = input().strip()
        if inputs[0] not in dic:
            dic[inputs[0]] = set()
        dic[inputs[0]].add(inputs)
    emeqhwkq(N2, dic)