# 수 조작하기 2
# 프로그래머스 L0 (기초·입문)
# 문제 링크: https://school.programmers.co.kr/learn/courses/30/lessons/181925
# 알고리즘: 조건문
# 작성자: 백관민
# 작성일: 2026. 07. 29. 10:37:58

def solution(numLog):
    a = ''
    for i in range(1,len(numLog)):
        b = numLog[i] - numLog[i-1]
        if b == 1:
            a += 'w'
        elif b == -1:
            a += 's'
        elif b == 10:
            a += 'd'
        else:
            a += 'a'
    return a
            