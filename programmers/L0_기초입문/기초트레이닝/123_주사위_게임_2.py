# 주사위 게임 2
# 프로그래머스 L0 (기초·입문)
# 문제 링크: https://school.programmers.co.kr/learn/courses/30/lessons/181930
# 알고리즘: 조건문
# 작성자: 백관민
# 작성일: 2026. 07. 24. 11:11:57

def solution(a, b, c):
    score1 = a + b + c
    score2 = a**2 + b**2 + c**2
    score3 = a**3 + b**3 + c**3

    if a == b == c:
        return score1 * score2 * score3
    elif a == b or b == c or a == c:
        return score1 * score2
    else:
        return score1