from collections import deque


def solution(priorities, location):
    answer = 1
    doc = deque([])
    q = deque([])
    for i in range(0, len(priorities)):
        doc.append(priorities[i])
        q.append(i)

    while True:
        print(doc)
        print(q)
        bot_doc = doc.popleft()
        bot_q = q.popleft()

        if len(doc) > 1 and bot_doc < max(doc):
            doc.append(bot_doc)
            q.append(bot_q)
        else:
            if bot_q == location:
                return answer
            answer += 1


print(solution([1], 0))
