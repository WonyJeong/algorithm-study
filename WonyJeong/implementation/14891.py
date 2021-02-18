import sys

input = sys.stdin.readline


def getRotate(idx, ori):
    newGier = [i for i in gier[idx]]

    if ori == 1:
        end = newGier.pop()
        newGier.insert(0, end)
    else:
        top = newGier[0]
        del newGier[0]
        newGier.append(top)

    return newGier


def recursive(idx, ori, memo, visited):
    if visited[idx] == False:
        visited[idx] = True
        memo[idx] = ori

        if idx > 0 and gier[idx - 1][2] != gier[idx][6]:
            recursive(idx - 1, ori * -1, memo, visited)

        if idx < 3 and gier[idx + 1][6] != gier[idx][2]:
            recursive(idx + 1, ori * -1, memo, visited)


def rotationGier():
    for idx, ori in rotation:
        memo = [0 for _ in range(4)]
        visited = [False for _ in range(4)]
        recursive(idx, ori, memo, visited)

        for i in range(0, 4):
            if memo[i] != 0:
                gier[i] = getRotate(i, memo[i])

    result = 0
    for i in range(4):
        result += gier[i][0] * (2 ** i)
    print(result)


if __name__ == "__main__":
    global gier, K, rotation
    gier = []
    for _ in range(4):
        gier.append(list(map(int, input().strip())))
    K = int(input().strip())
    rotation = []
    for _ in range(K):
        idx, ori = map(int, input().strip().split())
        rotation.append([idx - 1, ori])

    rotationGier()
