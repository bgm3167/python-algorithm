# 피자 나눠 먹기 (3)
# 프로그래머스 L0 (기초·입문)
# 문제 링크: https://school.programmers.co.kr/learn/courses/30/lessons/120816
# 알고리즘: 기초
# 작성자: 백관민
# 작성일: 2026. 07. 20. 10:06:00

import math as ma

def solution(slice, n):
    return ma.ceil(n/slice)