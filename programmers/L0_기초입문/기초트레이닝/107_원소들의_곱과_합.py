# 원소들의 곱과 합
# 프로그래머스 L0 (기초·입문)
# 문제 링크: https://school.programmers.co.kr/learn/courses/30/lessons/181929
# 알고리즘: 조건문
# 작성자: 백관민
# 작성일: 2026. 07. 24. 10:25:17

def solution(num_list):
    a = 1
    b = 0
    for i in num_list:
        a *= i
        b += i
    return (1 if a < (b**2) else 0)