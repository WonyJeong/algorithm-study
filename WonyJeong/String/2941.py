import sys

input = sys.stdin.readline

words = input().strip()
dict = ["c=", "c-", "dz=", "d-", "lj", "nj", "s=", "z="]

for w in dict:
    words = words.replace(w, "!")
print(len(words))
