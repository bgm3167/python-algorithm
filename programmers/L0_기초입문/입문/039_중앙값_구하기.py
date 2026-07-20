# 중앙값 구하기
# 프로그래머스 L0 (기초·입문)
# 문제 링크: https://school.programmers.co.kr/learn/courses/30/lessons/120811
# 알고리즘: 기초
# 작성자: 백관민
# 작성일: 2026. 07. 20. 12:28:30

import math as ma

def solution(array):
    array.sort()
    
    return array[ma.floor(len(array)/2)]
