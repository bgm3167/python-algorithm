# 간단한 논리 연산
# 프로그래머스 L0 (기초·입문)
# 문제 링크: https://school.programmers.co.kr/learn/courses/30/lessons/181917
# 알고리즘: 조건문
# 작성자: 백관민
# 작성일: 2026. 07. 30. 10:25:49

def solution(x1, x2, x3, x4):
    a = (int(x1)+int(x2)) * (int(x3)+int(x4))
    if a == 0:
        return False
    else:
        return True