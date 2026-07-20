# 제곱수 판별하기
# 프로그래머스 L0 (기초·입문)
# 문제 링크: https://school.programmers.co.kr/learn/courses/30/lessons/120909
# 알고리즘: 기초
# 작성자: 백관민
# 작성일: 2026. 07. 20. 11:29:52

def solution(n):
    if (n ** 0.5) == (n ** 0.5)//1:
        return 1
    else:
        return 2