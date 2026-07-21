# 369게임
# 프로그래머스 L0 (기초·입문)
# 문제 링크: https://school.programmers.co.kr/learn/courses/30/lessons/120891
# 알고리즘: 기초
# 작성자: 백관민
# 작성일: 2026. 07. 21. 10:23:25

def solution(order):
    answer = 0

    for i in str(order):
        if i in "369":
            answer += 1

    return answer