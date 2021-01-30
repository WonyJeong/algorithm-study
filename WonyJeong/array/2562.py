import sys

input = sys.stdin.readline

m_value = 0
m_idx = -1

for i in range(0, 9):
    temp = int(input().strip())
    if temp > m_value:
        m_value = temp
        m_idx = i + 1

print(m_value)
print(m_idx)