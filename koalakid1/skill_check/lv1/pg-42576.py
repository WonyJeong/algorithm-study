import collections


def solution(participant, completion):
    p = set(participant)
    c = set(completion)
    result = list(p-c)
    if result == []:
        count = collections.Counter(participant)
        for name, num in count.items():
            if completion.count(name) < num:
                return name
    return result[0]
