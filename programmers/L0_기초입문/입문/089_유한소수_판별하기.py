# 유한소수 판별하기
# 프로그래머스 L0 (기초·입문)
# 문제 링크: https://school.programmers.co.kr/learn/courses/30/lessons/120878
# 알고리즘: 기초
# 작성자: 백관민
# 작성일: 2026. 07. 23. 10:35:28

from math import gcd

def solution(a, b):
    g = gcd(a, b)
    b //= g

    while b % 2 == 0:
        b //= 2

    while b % 5 == 0:
        b //= 5

    if b == 1:
        return 1
    else:
        return 2
            
        