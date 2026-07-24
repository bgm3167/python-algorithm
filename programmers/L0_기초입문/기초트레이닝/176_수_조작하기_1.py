# 수 조작하기 1
# 프로그래머스 L0 (기초·입문)
# 문제 링크: https://school.programmers.co.kr/learn/courses/30/lessons/181926
# 알고리즘: 조건문
# 작성자: 백관민
# 작성일: 2026. 07. 24. 14:02:45

def solution(n, control):
    for i in control:
        if i == "w":
            n += 1
        elif i == "s":
            n -= 1
        elif i == "d":
            n += 10
        else:
            n -= 10
    return n