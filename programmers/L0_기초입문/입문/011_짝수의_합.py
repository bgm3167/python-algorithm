# 짝수의 합
# 프로그래머스 L0 (기초·입문)
# 문제 링크: https://school.programmers.co.kr/learn/courses/30/lessons/120831
# 알고리즘: 기초
# 작성자: 백관민
# 작성일: 2026. 07. 20. 09:33:34

def solution(n):
    a = 0

    for i in range(2, n + 1, 2):
        a += i

    return a