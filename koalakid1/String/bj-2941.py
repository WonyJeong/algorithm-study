import sys

input = sys.stdin.readline

string = input().strip()

another = ["c=", "c-", "dz=", "d-", "lj", "nj", "s=", "z="]

count = 0
alphaCount = 0
for i in another:
    alphaCount += string.count(i)
    count += string.count(i) * len(i)
    if i == "z=":
        alphaCount -= string.count("dz=")
        count -= string.count("dz=") * len(i)
print(alphaCount + len(string) - count)
