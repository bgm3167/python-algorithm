# 주사위 게임 1
# 프로그래머스 L0 (기초·입문)
# 문제 링크: https://school.programmers.co.kr/learn/courses/30/lessons/181839
# 알고리즘: 조건문 활용
# 작성자: 백관민
# 작성일: 2026. 07. 24. 15:58:54

def solution(a, b):
    if (a+b) % 2 == 0:
        if a % 2 == 0:
            return abs(a-b)
        else:
            return (a ** 2) + (b ** 2)
    return 2 * (a + b)