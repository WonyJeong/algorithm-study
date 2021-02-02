#4344
import sys
input = sys.stdin.readline
C = int(input().strip())
for i in range(0, C) :
    testcase = list(map(int, input().strip().split()))  #testcase[0] : numberOfStudents , testcase[1:] : students' score
    average = sum(testcase[1:])/testcase[0]
    count = 0
    for j in range(1,len(testcase)):
        if testcase[j] > average : count += 1
    print("%.3f"%round(count/testcase[0]*100,3), "%", sep='')